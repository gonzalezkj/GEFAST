from django.shortcuts import render
from AppArticulos.models import Articulo, Categoria

# Create your views here.

def stock(request): 
    articulo = Articulo.objects.all()
    categoria = Categoria.objects.all()
    queryset = request.GET.get("categoria")
    if queryset:
        articulo = Articulo.objects.filter(nombre = queryset)
    queryset = request.GET.get("buscarcat")
    if queryset:
        categoria = Categoria.objects.filter(nombre = queryset)
    queryset = request.GET.get("buscarprecio")
    querysete = request.GET.get("buscarprecio2")
    if queryset and querysete:
        articulo = Articulo.objects.filter(precio__gte = queryset, precio__lte = querysete)
    queryset = request.GET.get("buscarcant")
    querysete = request.GET.get("buscarcant2")
    if queryset and querysete:
        articulo = Articulo.objects.filter(cantidad__gte = queryset, cantidad__lte = querysete)
    return render(request, "AppStock/stock.html",  {"cat":categoria, "art":articulo})

def precio(request):
    articulo = Articulo.objects.all()
    categoria = Categoria.objects.all()
    queryset = request.GET.get("buscarart")
    querysete = request.GET.get("buscarart2")
    if queryset and querysete:
        articulo = Articulo.objects.filter(precio >= queryset and precio <= querysete)
    return render(request, "AppStock/stock.html",  {"cat":categoria, "art":articulo})

#NO PUDE FILTRAR POR CATEGORIA PORQUE VIENE DEL OTRO MODEL