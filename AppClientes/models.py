from django.db import models

class CondicionFiscal(models.Model):
    id_condicion_fiscal = models.IntegerField(primary_key = True)
    condicion_fiscal=models.CharField('Condicion', max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "CondFiscal"
        verbose_name_plural="CondFiscales"

    def __str__(self):
        return self.condicion_fiscal

class Clientes(models.Model):
    id_cliente = models.IntegerField('Nro de ID',primary_key = True)
    cuit=models.PositiveIntegerField()
    razon_nombre=models.CharField('Razon o nombre', max_length=50)
    condicion=models.ForeignKey(CondicionFiscal, on_delete=models.CASCADE)
    telefono=models.PositiveIntegerField('Teléfono')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Cliente"
        verbose_name_plural="Clientes"

    def __str__(self):
        return self.razon_nombre