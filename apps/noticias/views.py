from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Noticia
from .forms import Formulario_Noticia

# Create your views here.
def Home_Noticias(request):

	todas = Noticia.objects.all()

	contexto = {}

	contexto ['noticias'] = todas

	contexto ['fecha'] = '10-12-2023'
	
	return render(request, 'noticias/home_noticias.html', contexto)

class Home_Noticias_clase(ListView):
	model = Noticia
	template_name = 'noticias/home_noticias.html'
	context_object_name = 'noticias'

class Cargar_noticia(CreateView):
	model = Noticia
	template_name = 'noticias/cargar_noticia.html'
	form_class = Formulario_Noticia
	success_url = reverse_lazy('noticias:h_noticias')
