from django.shortcuts import redirect
from AppAgregar.agregar import Agregar
from AppAgregarCli.agregarcli import Agregarcli
from AppArticulos.models import Articulo
from AppFactura.models import ComprobanteV, DetalleV, PuntosDeVenta, TipoComprobante
from AppClientes.models import Clientes
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


"""
@login_required
def procesar_venta(request):
    agregar = Agregar(request)
    venta_lista = list()
    for key, value in agregar.agregar.items():
        venta_lista.append(
            DetalleV(
                articulo_id=key,
                cantidad=value["cantidad"],
                monto_unitario=value["precio"],
                id_cliente=
            )
        )
    
    DetalleV.objects.bulk_create(venta_lista)

    agregar.clear()

    messages.success(request, "La orden se creo correctamente.")
    return redirect("Home")

@login_required
def procesar_venta(request):
    agregar = Agregar(request)
    agregarcli = Agregarcli(request)
    venta_lista = list()
    venta_registro = list()
    for key, value in agregar.agregar.items():
        venta_lista.append(
            DetalleV(
                articulo_id=key,
                cantidad=value["cantidad"],
                monto_unitario=value["precio"],
            )
        )
    for key, value in agregarcli.agregarcli.items():
        venta_registro.append(
            ComprobanteV(
                articulo_id=key,
                cantidad=value["cantidad"],
                monto_unitario=value["precio"],
            )
        )
    
    DetalleV.objects.bulk_create(venta_lista)
    ComprobanteV.objects.bulk_create(venta_registro)

    agregar.clear()

    messages.success(request, "La orden se creo correctamente.")
    return redirect("Home")
"""