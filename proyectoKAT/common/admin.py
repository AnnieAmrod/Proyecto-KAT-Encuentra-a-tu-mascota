from django.contrib import admin
from .models import Provincia, Color

# Register your models here.

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capital', 'region')
    search_fields = ('nombre', 'capital')


class ColorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_hexadecimal', 'descripcion')
    search_fields = ('nombre', 'codigo_hexadecimal', 'descripcion')


admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Color, ColorAdmin)