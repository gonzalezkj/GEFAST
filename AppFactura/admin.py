from django.contrib import admin

from AppFactura.models import ComprobanteC, DetalleV, PuntosDeVenta, TipoComprobante, ComprobanteV

# Register your models here.

admin.site.register(TipoComprobante)
admin.site.register(ComprobanteC)
admin.site.register(ComprobanteV)
admin.site.register(DetalleV)
admin.site.register(PuntosDeVenta)