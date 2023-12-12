from django import forms
from .models import Noticia


class Formulario_Noticia(forms.ModelForm):

	class Meta:
		model = Noticia
<<<<<<< HEAD
		fields = ['titulo','contenido','imagen','categoria']

class Formulario_Modificar_Noticia(forms.ModelForm):

	class Meta:
		model = Noticia
		fields = ['contenido','imagen','categoria']		
=======
		fields = ['titulo','contenido','imagen','categoria']
>>>>>>> 44153ea4e5a98109987d83981a0304487e11cdc3
