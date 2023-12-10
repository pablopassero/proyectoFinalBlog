from django import forms
from .models import Noticia


class Formulario_Noticia(forms.ModelForm):

	class Meta:
		model = Noticia
		fields = ['titulo','contenido','imagen','categoria']