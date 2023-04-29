from django.contrib import admin

# Register your models here.
from .models import Especie, Raza, MLost, MFind, Aviso


class EspecieAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('nombre', 'nom_cientifico', 'descripcion')

class RazaAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('nombre', 'especie', 'origen')
    search_fields = ['nombre', 'especie', 'origen', 'longevidad', 'temperamento']

class MLostAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('nombre', 'especie', 'anio_nacimiento', 'raza', 'num_chip', 'devuelto')
    search_fields = ['nombre', 'especie', 'raza', 'num_chip']

class MFindAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('nombre', 'especie', 'devuelto')
    search_fields = ['nombre', 'especie']

class AvisoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('tipo_aviso', 'fecha_aviso', 'provincia', 'ciudad')
    search_fields = ['tipo_aviso', 'provincia', 'ciudad']


admin.site.register(Especie, EspecieAdmin)
admin.site.register(Raza, RazaAdmin)
admin.site.register(MLost, MLostAdmin)
admin.site.register(MFind, MFindAdmin)
admin.site.register(Aviso, AvisoAdmin)