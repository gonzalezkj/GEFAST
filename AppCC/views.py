from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AppFactura.models import ComprobanteC, TipoComprobante
from AppProveedores.models import Proveedores

# Create your views here.

@login_required
def cuentacorriente(request): 
    comprobantes = ComprobanteC.objects.all()
    tipocomprobante = TipoComprobante.objects.all()
    provs = Proveedores.objects.all()
    proveedores = Proveedores.objects.all()

    queryset = request.GET.get("razonsocial")
    print (queryset)
    if queryset:
        proveedores = Proveedores.objects.filter(razon_social = queryset)
    else:
        proveedores = Proveedores.objects.filter(id_proveedor = 1)

    return render(request, "AppCC/cuentacorriente.html", {"compro":comprobantes, "tipo":tipocomprobante, "prov": proveedores, "p":provs})
