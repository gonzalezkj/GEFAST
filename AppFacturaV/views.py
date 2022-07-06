from django.shortcuts import render, redirect
from AppAgregarF.agregarf import AgregarF
from AppArticulos.models import Articulo
from AppClientes.models import Clientes
from AppAgregarCli.agregarcli import Agregarcli
from AppFactura.models import ComprobanteC, DetalleC, PuntosDeVenta, TipoComprobante
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from AppAgregar.agregar import Agregar
from AppFactura.models import ComprobanteV, DetalleV, PuntosDeVenta, TipoComprobante
from django.contrib import messages

# Create your views here.

@login_required
def facturaventa(request): 
    articulo = Articulo.objects.all()
    cliente = Clientes.objects.all()
    facturas = TipoComprobante.objects.all()
    puntosdeventa = PuntosDeVenta.objects.all()
    p = Paginator(Articulo.objects.all(),4)
    page = request.GET.get('page')
    articulos = p.get_page(page)

    querysete = request.GET.get("buscarart")
    if querysete:
        articulo = Articulo.objects.filter(nombre = querysete)

    queryset = request.GET.get("buscarcli")
    if queryset:
        cliente = Clientes.objects.filter(razon_nombre = queryset)

    return render(request, "AppFacturaV/facturaventa.html",  {"cli":cliente, "art":articulo, "fact":facturas, "articulos":articulos, "puntos":puntosdeventa})


@login_required
def procesar_venta(request):
    agregar = Agregar(request)
    agregarcli = Agregarcli(request)
    agregarf = AgregarF(request)
    numerofact = request.GET.get("numerofact")
    for key, value in agregarf.agregarf.items():
        f = value["factura_id"]
    if f == 1 or f == 2 or f == 3:
        ivapor = 21
    else:
        ivapor = 0
    for key, value in agregarcli.agregarcli.items():
        cli = value["cliente_id"]
    for key, value in agregar.agregar.items():
        if f == 1 or f == 2 or f == 3:
            comprobante = ComprobanteV.objects.create(
                user=request.user, 
                numero=numerofact,
                id_punto_de_venta=request.GET.get("puntonumero"),
                id_tipo_comprobante=f,
                id_proveedor=cli,
                monto_total=(value["subtotal"]*21)/100+(value["subtotal"]),
            )
            break
        else:
            comprobante = ComprobanteV.objects.create(
                user=request.user, 
                numero=numerofact,
                id_punto_de_venta=request.GET.get("puntonumero"),
                id_tipo_comprobante=f,
                id_proveedor=cli,
                monto_total=value["subtotal"],
            )
    venta_lista = list() 
    for key, value in agregar.agregar.items():
        b = request.GET.get("bonif")
        if b == '':
            b = int(1)
        venta_lista.append(
            DetalleV(
                user=request.user,
                id_articulo=key,
                cantidad=value["cantidad"],
                monto_unitario=value["precio"],
                porcentaje_iva=ivapor,
                bonificacion=b,
                id_comprobante=comprobante,
                )
        )
    
    DetalleV.objects.bulk_create(venta_lista)

    agregar.clear()
    agregarcli.clearcli()

    messages.success(request, "La orden se creo correctamente.")
    return redirect("Home")