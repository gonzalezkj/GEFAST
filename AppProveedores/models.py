from django.db import models
from AppClientes.models import CondicionFiscal
from AppDirecciones.models import Direcciones

# Create your models here.

class Proveedores(models.Model):
    id_proveedor = models.IntegerField(primary_key = True)
    cuit = models.PositiveIntegerField()
    razon_social = models.CharField('Razón social', max_length=30)
    condicion = models.ForeignKey(CondicionFiscal, on_delete=models.CASCADE)
    telefono = models.CharField('Teléfono', max_length=30)
    email = models.EmailField('Email')
    direccion = models.ForeignKey(Direcciones, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.razon_social
    