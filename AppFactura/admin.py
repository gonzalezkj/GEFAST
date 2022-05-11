from django.contrib import admin

from AppFactura.models import ComprobanteC, TipoComprobante

# Register your models here.

admin.site.register(TipoComprobante)
admin.site.register(ComprobanteC)