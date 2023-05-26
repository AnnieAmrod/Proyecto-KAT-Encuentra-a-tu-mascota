from django import template
from ..models import Especie
register = template.Library()

@register.inclusion_tag('katapp/especie_mperdida_dropdown.html')
def especie_mperdida_dropdown():
    especies = Especie.objects.all()
    return {'especies': especies}