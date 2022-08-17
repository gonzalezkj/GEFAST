from django.shortcuts import render
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
from AppArticulos.models import Articulo, Categoria
from django.contrib import messages

# Create your views here.

@login_required
def stock(request): 
    articulo = Articulo.objects.all()
    categoria = Categoria.objects.all()

    queryset = request.GET.get("buscarcat")
    if queryset == 'Deportes':
        articulo = Articulo.objects.filter(categoria_id = 1)
    elif queryset == 'Ferreteria':
        articulo = Articulo.objects.filter(categoria_id = 2)
    elif queryset == 'Computacion':
        articulo = Articulo.objects.filter(categoria_id = 3)
    else:
        categoria = Categoria.objects.all()

    queryset = request.GET.get("buscarprecio")
    querysete = request.GET.get("buscarprecio2")
    if queryset and querysete:
        articulo = Articulo.objects.filter(precio__gte = queryset, precio__lte = querysete)

    queryset = request.GET.get("buscarcant")
    querysete = request.GET.get("buscarcant2")
    if queryset and querysete:
        articulo = Articulo.objects.filter(cantidad__gte = queryset, cantidad__lte = querysete)
        
    return render(request, "AppStock/stock.html",  {"cat":categoria, "art":articulo})


@login_required
def precio(request):
    articulo = Articulo.objects.all()
    categoria = Categoria.objects.all()
    queryset = request.GET.get("buscarart")
    querysete = request.GET.get("buscarart2")
    if queryset and querysete:
        articulo = Articulo.objects.filter(precio >= queryset and precio <= querysete)
    return render(request, "AppStock/stock.html",  {"cat":categoria, "art":articulo})


@login_required
def agregar_articulo(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El articulo se añadio correctamente")
        else:
            data["form"] = formulario
            
    return render(request, 'AppStock/agregar.html', data)