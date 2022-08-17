'''
from django.db import models
from AppProveedores.models import Proveedores
from AppFactura.models import ComprobanteC

# Create your models here.

class CCProveedor(models.Model):
    nombre = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    comprobante = models.ForeignKey(ComprobanteC, on_delete=models.CASCADE)
    saldo = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "CCProveedor"
        verbose_name_plural = "CCProveedores"

    def __str__(self):
        return self.nombre
'''