from tkinter import CASCADE
from django.db import models
from AppClientes.models import CondicionFiscal
from AppDirecciones.models import Direcciones

# Create your models here.

class ProveedorDirecciones(models.Model):
    id_proveedorDirecciones = models.IntegerField(primary_key = True)
    id_direccion = models.ForeignKey(Direcciones, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Direccion Proveedor"
        verbose_name_plural = "Direccion Proveedores"

    def __str__(self):
        return "Direccion Proveedores"

class Proveedores(models.Model):
    id_proveedor = models.IntegerField(primary_key = True)
    cuit = models.PositiveIntegerField()
    razon_social = models.CharField(max_length=30)
    condicion = models.ForeignKey(CondicionFiscal, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=30)
    email = models.EmailField()
    id_proveedorDirecciones = models.ForeignKey(ProveedorDirecciones, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.razon_social
    