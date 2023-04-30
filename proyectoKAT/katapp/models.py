from django.db import models
from common.models import Provincia, Color
from usuario.models import Usuario
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.
class Especie(models.Model):
    nombre = models.CharField(max_length=25, verbose_name='Nombre', unique=True, null=False, blank=False)
    nom_cientifico = models.CharField(max_length = 50, verbose_name='Nombre Científico', unique=True, null=False, blank=False)
    descripcion = models.TextField(verbose_name='Descripcion', max_length=255, null=True, blank=True)
    imagen = models.ImageField(verbose_name='Imagen', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Especies"

    def __str__(self):
        return self.nombre


class Raza(models.Model):
    nombre = models.CharField(max_length=25, verbose_name='Nombre', unique=True, null=False, blank=False)
    descripcion = models.TextField(verbose_name='Descripcion', max_length=255, null=True, blank=True)
    imagen = models.ImageField(verbose_name='Imagen', null=True, blank=True)
    especie = models.ForeignKey(Especie, verbose_name='Especie', on_delete=models.CASCADE, null=False, blank=False)
    origen = models.CharField(max_length=25, verbose_name='Origen', null=True, blank=True)
    peso_medio = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Peso Promedio', null=True, blank=True)
    altura_media = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Altura Promedio', null=True, blank=True)
    longevidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(40)], verbose_name='Esperanza de vida', null=True, blank=True) #Longevidad máxima de los gatos --> 38 años (perros --> 29 años)
#    nivel_actividad_choices = [
#        ('A', 'Alto'),
#        ('M', 'Medio'),
#        ('B', 'Bajo')
#    ]
#    actividad = models.CharField(max_length=1, choices=nivel_actividad_choices, default='M', null=False, blank=False) #Será un desplegable
    actividad = models.CharField(max_length=5, verbose_name='Nivel de Actividad', null=False, blank=False)
    temperamento = models.CharField(max_length=20, verbose_name='Temperamento', null=False, blank=False)

    class Meta:
        verbose_name_plural = "Razas"

    def __str__(self):
        return self.nombre


class MLost(models.Model):
    nombre = models.CharField(max_length=25, verbose_name='Nombre', null=False, blank=False)
    especie = models.ForeignKey(Especie, verbose_name='Especie', on_delete=models.CASCADE, null=False, blank=False)
    lugar_perdida = models.CharField(max_length=255, verbose_name='Lugar Pérdida', null=False, blank=False)
    foto = models.ImageField(max_length=80, verbose_name='Foto', null=False, blank=False)
    #descripcion = models.TextField(max_length=255, verbose_name='Descripción', null=False, blank=False)
    descripcion = RichTextField(verbose_name='Descripción', null=False, blank=False)
    color = models.ManyToManyField(Color, verbose_name='Color', related_name='mlosts_colors')
    sexo = models.CharField(max_length=1, verbose_name='Sexo', blank=True, null=True)
    anio_nacimiento = models.CharField(max_length=4, verbose_name='Año de nacimiento', blank=True, null=True)
    raza = models.ForeignKey(Raza, verbose_name='Raza', on_delete=models.CASCADE, null=False, blank=False)
    fecha_extravio = models.DateField(default=now, verbose_name='Fecha extravío', null=False, blank=False)
    datos_contacto = models.ForeignKey(Usuario, verbose_name='Datos de Contacto', on_delete=models.CASCADE, null=False, blank=False) #TODO Cuando tenga el modelo de usuario, descomentar
    tamano = models.CharField(max_length=10, verbose_name='Tamaño', blank=True, null=True)
    peso = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Peso', blank=True, null=True)
    num_chip = models.CharField(max_length=15, verbose_name='Número de Chip', unique=True, blank=True, null=True)
    pelo = models.CharField(max_length=5, verbose_name='Pelo', blank=True, null=True)
    collar = models.BooleanField(default=False)
    devuelto = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Mascota Perdida"
        verbose_name_plural = "Mascotas Perdidas"

    def __str__(self):
        return self.nombre


class MFind(models.Model):
    nombre = models.CharField(max_length=25, verbose_name='Nombre', null=True, blank=True)
    especie = models.ForeignKey(Especie, verbose_name='Especie', on_delete=models.CASCADE, null=False, blank=False)
    lugar_encontrado = models.CharField(max_length=255, verbose_name='Lugar Encontrado', null=False, blank=False)
    foto = models.ImageField(max_length=80, verbose_name='Foto', null=False, blank=False)
    descripcion = models.TextField(max_length=255, verbose_name='Descripción', null=False, blank=False)
    color = models.ManyToManyField(Color, verbose_name='Color', related_name='mfinds_colors')
    sexo = models.CharField(max_length=1, verbose_name='Sexo', blank=True, null=True)
    raza = models.ForeignKey(Raza, verbose_name='Raza', on_delete=models.CASCADE, null=True, blank=True)
    fecha_encontrado = models.DateField(default=now, verbose_name='Fecha encontrado', null=False, blank=False)
    datos_contacto = models.ForeignKey(Usuario, verbose_name='Datos de Contacto', on_delete=models.CASCADE, null=False, blank=False) #TODO Cuando tenga el modelo de usuario, descomentar
    tamano = models.CharField(max_length=10, verbose_name='Tamaño', blank=True, null=True)
    num_chip = models.CharField(max_length=15, verbose_name='Número de Chip', unique=True, blank=True, null=True)
    pelo = models.CharField(max_length=5, verbose_name='Pelo', blank=True, null=True)
    collar = models.BooleanField(default=False)
    devuelto = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Mascota encontrada"
        verbose_name_plural = "Mascotas encontradas"

    def __str__(self):
        return self.nombre


class Aviso(models.Model):
    razon = models.CharField(max_length=20, verbose_name='Razón', blank=False, null=False)
    tipo_aviso = models.CharField(max_length=20, verbose_name='Tipo de aviso', blank=False, null=False)
    fecha_aviso = models.DateField(default=now, verbose_name='Fecha de aviso', blank=False, null=False)
    hora_aviso = models.TimeField(default=now, verbose_name='Hora de aviso', blank=False, null=False)
    ubicacion = models.CharField(max_length=255, verbose_name='Ubicación', blank=False, null=False)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name='Provincia', blank=False, null=False)
    ciudad = models.CharField(max_length=30, verbose_name='Ciudad', blank=False, null=False)
    imagen = models.CharField(max_length=80, verbose_name='Imagen', blank=False, null=False)
    descripcion = models.TextField(max_length=255, verbose_name='Descripción', null=False, blank=False)
    contacto = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Contacto', blank=False, null=False)

    class Meta:
        verbose_name_plural = "Avisos"

    def __str__(self):
        return self.nombre