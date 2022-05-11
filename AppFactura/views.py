from django.shortcuts import render
from AppArticulos.models import Articulo
from AppClientes.models import Clientes
from AppFactura.models import TipoComprobante

# Create your views here.

def factura(request): 
    articulo = Articulo.objects.all()
    cliente = Clientes.objects.all()
    facturas = TipoComprobante.objects.all()
    querysete = request.GET.get("buscarart")
    if querysete:
        articulo = Articulo.objects.filter(nombre = querysete)
    queryset = request.GET.get("buscarcli")
    if queryset:
        cliente = Clientes.objects.filter(razon_nombre = queryset)
    return render(request, "AppFactura/factura.html",  {"cli":cliente, "art":articulo, "fact":facturas})