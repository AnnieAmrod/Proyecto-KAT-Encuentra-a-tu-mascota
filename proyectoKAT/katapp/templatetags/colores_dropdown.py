from django import template
from ..models import Color
register = template.Library()

@register.inclusion_tag('katapp/color_dropdown.html')
def color_dropdown():
    colores = Color.objects.all()
    return {'colores': colores}