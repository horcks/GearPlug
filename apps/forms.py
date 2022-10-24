from django import forms
from .models import *

class personajeForm(forms.ModelForm):
	class Meta:
		model = personaje
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super(personajeForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

class peliculaForm(forms.ModelForm):
	class Meta:
		model = pelicula
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(peliculaForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

class planetaForm(forms.ModelForm):
	class Meta:
		model = planeta
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		print(kwargs.pop('request'))
		super(planetaForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'