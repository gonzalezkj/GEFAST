from django.shortcuts import redirect
from AppProveedores.models import Proveedores
from AppClientes.models import Clientes
from .agregarprov import Agregarprov
# Create your views here.

def addprov(request, prov_id):
    agregar = Agregarprov(request)
    proveedor = Proveedores.objects.get(id_proveedor=prov_id)
    agregar.addprov(proveedor=proveedor)
    return redirect(request.META.get('HTTP_REFERER', 'Proveedores'))

def removeprov(request, prov_id):
    agregar = Agregarprov(request)
    proveedor = Proveedores.objects.get(id_proveedor=prov_id)
    agregar.removeprov(proveedor=proveedor)
    return redirect(request.META.get('HTTP_REFERER', 'Proveedores'))

def clearprov(request):
    agregar = Agregarprov(request)
    agregar.clearprov()
    return redirect(request.META.get('HTTP_REFERER', 'Proveedores'))
