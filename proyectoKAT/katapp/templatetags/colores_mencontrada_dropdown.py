from django import template
from ..models import Color
register = template.Library()

@register.inclusion_tag('katapp/color_mencontrada_dropdown.html')
def color_mencontrada_dropdown():
    colores = Color.objects.all()
    return {'colores': colores}