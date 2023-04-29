from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from common.models import Provincia

# Create your models here.
class UsuarioPersonalizado(BaseUserManager):
    def create_user(self, email, nombre, apellido1, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser obligatorio')

        usuario = self.model(
            email=self.normalize_email(email),
            nombre=nombre,
            apellido1=apellido1,
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, nombre, apellido1, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nombre, apellido1, password, **extra_fields)


class Usuario(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email', unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=25, verbose_name='Nombre', null=False, blank=False) #Requerido en la base de datos y en los formularios
    apellido1 = models.CharField(max_length=25, verbose_name='Primer Apellido', null=False, blank=False)
    apellido2 = models.CharField(max_length=25, verbose_name='Segundo Apellido', null=True, blank=True)
    direccion = models.CharField(max_length=100, verbose_name='Dirección', null=False, blank=False)
    ciudad = models.CharField(max_length=30, verbose_name='Ciudad', null=False, blank=False)
    cod_postal = models.CharField(max_length=5, verbose_name='Código Postal', null=False, blank=False)
    provincia = models.ForeignKey(Provincia, verbose_name='Provincia', on_delete=models.CASCADE, null=True, blank=True)
    telefono = models.CharField(max_length=20, verbose_name='Teléfono', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido1']

    objects = UsuarioPersonalizado()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True