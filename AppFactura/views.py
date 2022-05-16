from django.shortcuts import render
from AppArticulos.models import Articulo
from AppClientes.models import Clientes
from AppFactura.models import TipoComprobante
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

@login_required
def factura(request): 
    articulo = Articulo.objects.all()
    cliente = Clientes.objects.all()
    facturas = TipoComprobante.objects.all()
    p = Paginator(Articulo.objects.all(),4)
    page = request.GET.get('page')
    articulos = p.get_page(page)
    querysete = request.GET.get("buscarart")
    if querysete:
        articulo = Articulo.objects.filter(nombre = querysete)
    queryset = request.GET.get("buscarcli")
    if queryset:
        cliente = Clientes.objects.filter(razon_nombre = queryset)
    return render(request, "AppFactura/factura.html",  {"cli":cliente, "art":articulo, "fact":facturas, "articulos":articulos})