from django.shortcuts import render

# Create your views here.

def articulos(request): 
    return render(request, "AppArticulos/articulos.html")