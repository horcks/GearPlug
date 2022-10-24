from django.urls import path
from django.contrib.auth.decorators import login_required
from django_filters.views import object_filter
from .models import *
from django_filters.views import FilterView
from .views import *
urlpatterns = [
    path("", list_url.as_view(), name="index"),
    #listar
    path("list/personajes", FilterView.as_view(model=personaje), name="personajes-list"),
    path("list/peliculas", FilterView.as_view(model=pelicula), name="peliculas-list"),
    path("list/planetas", FilterView.as_view(model=planeta), name="planetas-list"),
    #Crear
    path("add/personajes", login_required(add_personaje.as_view()), name="personajes-add"),
    #path("add/peliculas", add_pelicula.as_view(), name="product-add"),
    #path("add/planetas", add_planeta.as_view(), name="product-list"),
]