from distutils import text_file
from django.db import models
from django.forms import CharField
import django_filters

# Create your models here.
class planeta(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.nombre)

class pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    texto_apertura = models.TextField()
    director = models.CharField(max_length=100)
    productor = models.CharField(max_length=100)
    planetas = models.ManyToManyField(planeta)
    def __str__(self):
        return '{}'.format(self.titulo)

class personaje(models.Model):    
    nombre = models.CharField(max_length=50)
    altura = models.IntegerField()
    masa = models.IntegerField()
    color_pelo = models.CharField(max_length=50)
    color_piel = models.CharField(max_length=50)
    color_ojos = models.CharField(max_length=50)
    año_nacimiento = models.IntegerField()
    genero = models.CharField(max_length=50)
    mundo_natal = models.ForeignKey(planeta, verbose_name=("mundo_natal"), on_delete=models.CASCADE)
    peliculas_participa = models.ManyToManyField(pelicula, verbose_name=("peliculas"))
    def __str__(self):
        return '{}'.format(self.nombre)
class personajeFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = personaje
        fields = ['nombre', ]