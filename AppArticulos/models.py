from django.db import models
# Create your models here.


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key = True)
    nombre = models.CharField('Categoria', max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    id_articulo=models.IntegerField(primary_key = True)
    nombre=models.CharField('Nombre', max_length=50)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio=models.FloatField('Precio')
    disponibilidad=models.BooleanField(default=True)
    cantidad=models.IntegerField('Cantidad')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Articulo"
        verbose_name_plural="Articulos"

    def __str__(self):
        return self.nombre 
