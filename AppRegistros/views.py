from django.shortcuts import render
from AppFactura.models import ComprobanteC, ComprobanteV, TipoComprobante, DetalleC
from AppArticulos.models import Articulo
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from AppProveedores.models import Proveedores
import pdfkit

# Create your views here.

def registros(request): 
    registrocompra = ComprobanteC.objects.all()
    tipocomprobante = TipoComprobante.objects.all() 
    proveedor = Proveedores.objects.all()
    return render(request, "AppRegistros/registros.html", {'regcom':registrocompra, 'tipo':tipocomprobante, 'prov':proveedor})

def registrosventa(request): 
    registroventa = ComprobanteV.objects.all()
    tipocomprobante = TipoComprobante.objects.all() 

    return render(request, "AppRegistros/registrosventa.html", {'regven':registroventa, 'tipo':tipocomprobante})

def selectcompra(request, id):
    comprobante = get_object_or_404(ComprobanteC, id = id)
    detalle = DetalleC.objects.all()
    articulo = Articulo.objects.all() 
    proveedor = Proveedores.objects.all()
    tip = TipoComprobante.objects.all()

    return render(request, "AppRegistros/selectcompra.html", {'comproc':comprobante, 'deta':detalle, 'art':articulo, 'tipocompro':tip, 'prov':proveedor})

def pdf(request, id):
    t = get_object_or_404(ComprobanteC, id=id)
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }

    pdf = pdfkit.from_url('http://127.0.0.1:8000/registros/selectcompra/'+str(t.id), False, options=options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="documento.pdf"'
    return response