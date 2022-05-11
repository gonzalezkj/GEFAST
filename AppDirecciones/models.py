from django.db import models

# Create your models here.

class Paises(models.Model):
    id_pais = models.IntegerField(primary_key = True) 
    nombre = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural="Paises"

    def __str__(self):
        return self.nombre

class Provincias(models.Model):
    id_provincia = models.IntegerField(primary_key = True) 
    nombre = models.CharField(max_length=30)
    id_pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural="Provincias"

    def __str__(self):
        return self.nombre

class Localidades(models.Model):
    id_localidad = models.IntegerField(primary_key = True) 
    nombre = models.CharField(max_length=30)
    id_provincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)
    codigo_postal = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural="Localidades"

    def __str__(self):
        return self.nombre

class Direcciones(models.Model):
    id_direccion = models.IntegerField(primary_key = True) 
    id_localidad = models.ForeignKey(Localidades, on_delete=models.CASCADE)
    calle = models.CharField(max_length=40)
    numero = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural="Direcciones"

    def __str__(self):
        return self.calle #Poner el numero dsp
