from django.db import models

from AppProveedores.models import Proveedores

# Create your models here.

class TipoComprobante(models.Model):
    id_tipo_comprobante = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=50)
    letra = models.CharField(max_length=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "TipoComprobante"
        verbose_name_plural = "TipoComprobantes"

    def __str__(self):
        return self.nombre+" "+self.letra

class ComprobanteC (models.Model):
    id_comprobante = models.IntegerField(primary_key = True)
    numero = models.IntegerField()
    id_punto_de_venta = models.IntegerField()
    id_tipo_comprobante = models.ForeignKey(TipoComprobante, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ComprobanteC"
        verbose_name_plural = "ComprobantesC"

    def __str__(self):
        return self.numero