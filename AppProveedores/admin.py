from django.contrib import admin
from AppProveedores.models import ProveedorDirecciones, Proveedores

# Register your models here.

admin.site.register(Proveedores)
admin.site.register(ProveedorDirecciones)