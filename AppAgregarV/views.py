from django.shortcuts import redirect
from .agregarv import AgregarV
from AppArticulos.models import Articulo

# Create your views here.

def add(request, articulo_id):
    agregarv = AgregarV(request)
    articulo = Articulo.objects.get(id_articulo=articulo_id)
    agregarv.add(articulo=articulo)
    return redirect(request.META.get('HTTP_REFERER', 'Articulos'))

def remove(request, articulo_id):
    agregarv = AgregarV(request)
    articulo = Articulo.objects.get(id_articulo=articulo_id)
    agregarv.remove(articulo=articulo)
    return redirect(request.META.get('HTTP_REFERER', 'Articulos'))

def decrement(request, articulo_id):
    agregarv = AgregarV(request)
    articulo = Articulo.objects.get(id_articulo=articulo_id)
    agregarv.decrement(articulo=articulo)
    return redirect(request.META.get('HTTP_REFERER', 'Articulos'))

def clear(request):
    agregarv = AgregarV(request)
    agregarv.clear()
    return redirect(request.META.get('HTTP_REFERER', 'Articulos'))
