from datetime import date, datetime
from django.shortcuts import render
from AppFactura.models import DetalleV, ComprobanteC
from AppArticulos.models import Articulo


# Create your views here.

def reportes(request):

    detalles = DetalleV.objects.all()
    articulos = Articulo.objects.all()
    comprobantes = ComprobanteC.objects.filter(date__range=["2022-07-01", datetime.now])
    
    productos = [0,0,0,0,0,0,0,0]
    for det in detalles:
        if det.id_articulo == 1:
            productos[0] = productos[0] + det.cantidad
        elif det.id_articulo == 2:
            productos[1] = productos[1] + det.cantidad
        elif det.id_articulo == 3:
            productos[2] = productos[2] + det.cantidad
        elif det.id_articulo == 4:
            productos[3] = productos[3] + det.cantidad
        elif det.id_articulo == 5:
            productos[4] = productos[4] + det.cantidad
        elif det.id_articulo == 6:
            productos[5] = productos[5] + det.cantidad
        elif det.id_articulo == 7:
            productos[6] = productos[6] + det.cantidad
        else:
            productos[7] = productos[7] + det.cantidad



    return render(request, "AppReportes/reportes.html", {'det':detalles, 'prod':productos, 'art':articulos, 'compro':comprobantes})
