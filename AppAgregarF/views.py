from django.shortcuts import redirect
from .agregarf import AgregarF
from AppFactura.models import TipoComprobante
# Create your views here.

def addf(request, factura_id):
    agregarf = AgregarF(request)
    factura = TipoComprobante.objects.get(id_tipo_comprobante=factura_id)
    agregarf.addf(factura=factura)
    return redirect(request.META.get('HTTP_REFERER', 'TipoComprobante'))

def clearf(request):
    agregar = AgregarF(request)
    agregar.clearf()
    return redirect(request.META.get('HTTP_REFERER', 'TipoComprobante'))