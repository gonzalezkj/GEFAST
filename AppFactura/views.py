from django.shortcuts import render, redirect
from AppAgregarF import agregarf
from AppAgregarF.agregarf import AgregarF
from AppArticulos.models import Articulo
from AppClientes.models import Clientes
from AppAgregarCli.agregarcli import Agregarcli
from AppFactura.models import PuntosDeVenta, TipoComprobante
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from AppAgregar.agregar import Agregar
from AppFactura.models import ComprobanteV, DetalleV, PuntosDeVenta, TipoComprobante
from django.contrib import messages

# Create your views here.

@login_required
def factura(request): 
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
    return render(request, "AppFactura/factura.html",  {"cli":cliente, "art":articulo, "fact":facturas, "articulos":articulos, "puntos":puntosdeventa})

#La FACTURA E es solo para servicios?

@login_required
def procesar_venta(request):
    agregar = Agregar(request)
    agregarcli = Agregarcli(request)
    agregarf = AgregarF(request)
    for key, value in agregarf.agregarf.items():
        f = value["factura_id"]
    if f == 1 or f == 2 or f == 3:
        ivapor = 21
    else:
        ivapor = 0
    for key, value in agregarcli.agregarcli.items():
        cli = value["cliente_id"]
    comprobante = ComprobanteV.objects.create(
        user=request.user, 
        id_puntoventa=request.GET.get("puntonumero"),
        id_tipocomprobante=f,
        id_cliente=cli,
        completed=True,
    )
    venta_lista = list() 
    for key, value in agregar.agregar.items():
        b = request.GET.get("bonif")
        if b == '':
            b = int(0)
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