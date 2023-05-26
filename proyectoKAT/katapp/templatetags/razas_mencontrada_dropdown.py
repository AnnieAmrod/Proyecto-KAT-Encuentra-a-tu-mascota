from django import template
from ..models import Raza
register = template.Library()

@register.inclusion_tag('katapp/raza_mencontrada_dropdown.html')
def raza_mencontrada_dropdown():
    razas = Raza.objects.all()
    return {'razas': razas}