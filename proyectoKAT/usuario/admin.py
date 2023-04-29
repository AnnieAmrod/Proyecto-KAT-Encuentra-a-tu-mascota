from django.contrib import admin

# Register your models here.
from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('email', 'nombre', 'apellido1', 'telefono', 'is_superuser')
    search_fields = ['email', 'nombre', 'ciudad', 'cod_postal']


admin.site.register(Usuario, UsuarioAdmin)