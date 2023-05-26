from django import template
from ..models import Provincia
register = template.Library()

@register.inclusion_tag('katapp/provincia_aviso_dropdown.html')
def provincia_aviso_dropdown():
    provincias = Provincia.objects.all()
    return {'provincias': provincias}