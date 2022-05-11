from django.shortcuts import redirect
from .agregar import Agregar
from AppArticulos.models import Articulo

# Create your views here.

def add(request, articulo_id):
    agregar = Agregar(request)
    articulo = Articulo.objects.get(id_articulo=articulo_id)
    agregar.add(articulo=articulo)
    return redirect(request.META.get('HTTP_REFERER', 'Articulos'))

def remove(request, articulo_id):
    agregar = Agregar(request)
    articulo = Articulo.objects.get(id_articulo=articulo_id)
    agregar.remove(articulo=articulo)
    return redirect(request.META.get('HTTP_REFERER', 'Articulos'))

def decrement(request, articulo_id):
    agregar = Agregar(request)
    articulo = Articulo.objects.get(id_articulo=articulo_id)
    agregar.decrement(articulo=articulo)
    return redirect(request.META.get('HTTP_REFERER', 'Articulos'))

def clear(request):
    agregar = Agregar(request)
    agregar.clear()
    return redirect(request.META.get('HTTP_REFERER', 'Articulos'))
