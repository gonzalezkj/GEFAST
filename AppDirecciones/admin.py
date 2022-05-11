from django.contrib import admin
from AppDirecciones.models import Direcciones, Localidades, Paises, Provincias

# Register your models here.

admin.site.register(Paises)
admin.site.register(Provincias)
admin.site.register(Localidades)
admin.site.register(Direcciones)