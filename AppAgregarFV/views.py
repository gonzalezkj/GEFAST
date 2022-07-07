from django.shortcuts import redirect
from .agregarfv import AgregarFV
from AppFactura.models import TipoComprobante
# Create your views here.

def addfv(request, factura_id):
    agregarfv = AgregarFV(request)
    factura = TipoComprobante.objects.get(id_tipo_comprobante=factura_id)
    agregarfv.addfv(factura=factura)
    return redirect(request.META.get('HTTP_REFERER', 'TipoComprobante'))

def clearfv(request):
    agregarfv = AgregarFV(request)
    agregarfv.clearfv()
    return redirect(request.META.get('HTTP_REFERER', 'TipoComprobante'))