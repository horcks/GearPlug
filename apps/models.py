from django.db import models
from django.forms import CharField

# Create your models here.
class planeta(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.nombre)

class actor(models.Model):    
    nombre = models.CharField(max_length=50)
    altura = models.IntegerField()
    masa = models.IntegerField()
    color_pelo = models.CharField(max_length=50)
    color_piel = models.CharField(max_length=50)
    color_ojos = models.CharField(max_length=50)
    año_nacimiento = models.IntegerField()
    género = models.CharField(max_length=50)
    mundo_natal = models.ForeignKey(planeta, verbose_name=("mundo_natal"), on_delete=models.CASCADE)
    #peliculas_participa = models.ManyToManyField(planeta, verbose_name=("peliculas"))