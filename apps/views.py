from django.shortcuts import render
from .forms import *
from django.views.generic.edit import FormView,CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
# Create your views here.
class add_personaje(CreateView):
    model = personaje
    form_class = personajeForm
    template_name = 'apps/add_personaje.html'
    success_url = reverse_lazy('apps:index')



class list_url(TemplateView):
    template_name = "apps/list_url.html"
