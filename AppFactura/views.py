from django.shortcuts import render, redirect
from AppAgregarF.agregarf import AgregarF
from AppArticulos.models import Articulo
from AppProveedores.models import Proveedores
from AppClientes.models import CondicionFiscal
from AppArticulos.models import Articulo
from AppAgregarProv.agregarprov import Agregarprov
from AppFactura.models import ComprobanteC, DetalleC, PuntosDeVenta, TipoComprobante
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from AppAgregar.agregar import Agregar
from AppFactura.models import ComprobanteV, DetalleV, PuntosDeVenta, TipoComprobante
from django.contrib import messages

# Create your views here.

@login_required
def factura(request): 
    articulo = Articulo.objects.all()    
    proveedores = Proveedores.objects.all()
    facturas = TipoComprobante.objects.all()
    puntosdeventa = PuntosDeVenta.objects.all()
    condicion = CondicionFiscal.objects.all()
    articulosprueba = Articulo.objects.get_queryset().order_by('id_articulo')
    p = Paginator(articulosprueba, 4)
    page = request.GET.get('page')
    articulos = p.get_page(page)

    querysete = request.GET.get("buscarart")
    if querysete:
        articulo = Articulo.objects.filter(nombre = querysete)

    queryset = request.GET.get("buscarprov")
    if queryset:
        proveedores = Proveedores.objects.filter(razon_social = queryset)

    return render(request, "AppFactura/factura.html",  {"prov":proveedores, "art":articulo, "fact":facturas, "articulos": articulos, "puntos":puntosdeventa, "condicion":condicion})


@login_required
def procesar_compra(request):
    agregar = Agregar(request)
    agregarprov = Agregarprov(request)
    agregarf = AgregarF(request)
    numerofact = request.GET.get("numerofact")
    monton = 0
    montonsiniva = 0
    f = 1
    for key, value in agregarf.agregarf.items():
        f = value["factura_id"]
    if f == 1 or f == 2 or f == 3:
        ivapor = 21
    else:
        ivapor = 0
    for key, value in agregarprov.agregarprov.items():
        prov = value["proveedor_id"]
    for key, value in agregar.agregar.items():
        monton = monton + value['totalcant']
        montonsiniva = montonsiniva + value['subtotal']
    if f == 1 or f == 2 or f == 3:
        comprobante = ComprobanteC.objects.create(
            user=request.user, 
            numero=numerofact,
            id_punto_de_venta=request.GET.get("puntonumero"),
            id_tipo_comprobante=f,
            id_proveedor=prov,
            monto_total=monton,
        )
    else:
        comprobante = ComprobanteC.objects.create(
            user=request.user, 
            numero=numerofact,
            id_punto_de_venta=request.GET.get("puntonumero"),
            id_tipo_comprobante=f,
            id_proveedor=prov,
            monto_total=montonsiniva,
        )

    if f == 1 or f == 2 or f == 3:
        venta_lista = list() 
        for key, value in agregar.agregar.items():
            b = request.GET.get("bonif")
            if b == '':
                b = int(1)
            venta_lista.append(
                DetalleC(
                    user=request.user,
                    id_articulo=key,
                    cantidad=value["cantidad"],
                    monto_unitario=value["precio"],
                    porcentaje_iva=ivapor,
                    bonificacion=b,
                    subtotal=value["subtotal"]*1.21,
                    id_comprobante=comprobante,
                    )
            )
    else:
        venta_lista = list() 
        for key, value in agregar.agregar.items():
            b = request.GET.get("bonif")
            if b == '':
                b = int(1)
            venta_lista.append(
                DetalleC(
                    user=request.user,
                    id_articulo=key,
                    cantidad=value["cantidad"],
                    monto_unitario=value["precio"],
                    porcentaje_iva=ivapor,
                    bonificacion=b,
                    subtotal=value["subtotal"],
                    id_comprobante=comprobante,
                    )
            )
    
    DetalleC.objects.bulk_create(venta_lista)

    agregar.clear()
    agregarprov.clearprov()

    messages.success(request, "La orden se creo correctamente.")
    return redirect("Home")
