from django import template
from ..models import Especie
register = template.Library()

@register.inclusion_tag('katapp/filtros_dropdown.html')
def especie_dropdown():
    especies = Especie.objects.all()
    return {'especies': especies}