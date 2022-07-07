from django.db import models
from AppArticulos.models import Articulo
from AppClientes.models import Clientes
from AppProveedores.models import Proveedores
from django.contrib.auth import get_user_model

User = get_user_model()

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

class PuntosDeVenta(models.Model):
    id_punto_de_venta = models.IntegerField(primary_key = True)
    numero = models.IntegerField()

    class Meta:
        verbose_name = "PuntoDeVenta"
        verbose_name_plural = "PuntoDeVentas"

    def __str__(self):
        return "Punto de venta nro " + (str(self.numero))

class ComprobanteC (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    id_punto_de_venta = models.IntegerField()
    id_tipo_comprobante =  models.IntegerField()
    id_proveedor = models.IntegerField()
    monto_total = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ComprobanteC"
        verbose_name_plural = "ComprobantesC"

    def __str__(self):
        return self.numero

class DetalleC (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_articulo = models.IntegerField()
    cantidad = models.IntegerField()
    monto_unitario = models.FloatField()
    porcentaje_iva = models.FloatField()
    bonificacion = models.IntegerField()
    id_comprobante = models.ForeignKey(ComprobanteC, on_delete=models.CASCADE)

    def __str__(self):
        return 'Detalle de '+(str(self.id_comprobante))

    class Meta:
        verbose_name = "Detalle"
        verbose_name_plural = "DetalleCompras"
        ordering = ['id']

class ComprobanteV (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_puntoventa = models.IntegerField()
    id_tipocomprobante = models.IntegerField()
    id_cliente = models.IntegerField()
    monto_total = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Orden número '+str(self.id)

    class Meta:
        verbose_name = "ComprobanteV"
        verbose_name_plural = "ComprobantesV"
        ordering = ['id']

class DetalleV (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_articulo = models.IntegerField()
    cantidad = models.IntegerField()
    monto_unitario = models.FloatField()
    porcentaje_iva = models.FloatField()
    bonificacion = models.IntegerField()
    id_comprobante = models.ForeignKey(ComprobanteV, on_delete=models.CASCADE)

    def __str__(self):
        return 'Detalle de '+(str(self.id_comprobante))

    class Meta:
        verbose_name = "Detalle"
        verbose_name_plural = "DetalleVentas"
        ordering = ['id']