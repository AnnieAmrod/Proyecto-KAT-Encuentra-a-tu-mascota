from django import template
from ..models import Raza
register = template.Library()

@register.inclusion_tag('katapp/raza_dropdown.html')
def raza_dropdown():
    razas = Raza.objects.all()
    return {'razas': razas}