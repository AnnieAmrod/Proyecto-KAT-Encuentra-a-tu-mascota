import django_filters

from .models import MLost, Especie, Color, Raza

class MLostFilter(django_filters.FilterSet):
    especie = django_filters.ModelChoiceFilter(field_name='especie__nombre', queryset=Especie.objects.all())
    lugar_perdida = django_filters.CharFilter(lookup_expr='icontains', label='Ubicación')
    color = django_filters.ModelMultipleChoiceFilter(field_name='color__nombre', queryset=Color.objects.all(), conjoined=True)
    raza = django_filters.ModelChoiceFilter(field_name='raza__nombre', queryset=Raza.objects.all())
    tamano = django_filters.CharFilter(lookup_expr='icontains', label='Tamaño')
    pelo = django_filters.CharFilter(lookup_expr='icontains', label='Pelo')

    class Meta:
        model = MLost
        fields = ['especie', 'lugar_perdida', 'color', 'raza', 'tamano', 'pelo']