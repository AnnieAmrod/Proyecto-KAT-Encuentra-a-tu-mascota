from django.db import models

# Create your models here.
class Provincia(models.Model):
    nombre = models.CharField(max_length=25, verbose_name='Nombre', unique=True, null=False, blank=False)
    capital = models.CharField(max_length=25, verbose_name='Capital', null=False, blank=False)
    region = models.CharField(max_length=25, verbose_name='Región', null=False, blank=False)

    class Meta:
        verbose_name_plural = "Provincias"

    def __str__(self):
        return self.nombre


class Color(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre del color", unique=True, null=False, blank=False)
    codigo_hexadecimal = models.CharField(max_length=7, verbose_name="Código hexadecimal del color", null=False, blank=False)
    descripcion = models.TextField(max_length=255, verbose_name="Descripción del color", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Colores"

    def __str__(self):
        return self.nombre