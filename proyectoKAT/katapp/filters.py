import django_filters

from .models import MLost, Especie

class MLostFilter(django_filters.FilterSet):
    especie = django_filters.ModelChoiceFilter(field_name='especie__nombre', queryset=Especie.objects.all())
    lugar_perdida = django_filters.CharFilter(lookup_expr='icontains', label='Ubicación')

    class Meta:
        model = MLost
        fields = ['especie', 'lugar_perdida']