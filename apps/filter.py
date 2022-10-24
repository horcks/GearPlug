import django_filters
from  .models import *
class personajeFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = personaje
        fields = ['nombre', ]
    
class peliculaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = pelicula
        fields = ['nombre', ]

class planetaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = planeta
        fields = ['nombre', ]