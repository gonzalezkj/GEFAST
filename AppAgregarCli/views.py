from django.shortcuts import redirect
from AppClientes.models import Clientes
from .agregarcli import Agregarcli
# Create your views here.

def addcli(request, cliente_id):
    agregar = Agregarcli(request)
    cliente = Clientes.objects.get(id_cliente=cliente_id)
    agregar.addcli(cliente=cliente)
    return redirect(request.META.get('HTTP_REFERER', 'Clientes'))

def removecli(request, cliente_id):
    agregar = Agregarcli(request)
    cliente = Clientes.objects.get(id_cliente=cliente_id)
    agregar.removecli(cliente=cliente)
    return redirect(request.META.get('HTTP_REFERER', 'Clientes'))

def clearcli(request):
    agregar = Agregarcli(request)
    agregar.clearcli()
    return redirect(request.META.get('HTTP_REFERER', 'Clientes'))
