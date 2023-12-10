
from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.Home_Noticias_clase.as_view(), name="h_noticias"),
    path('cargar/', views.Cargar_noticia.as_view(), name ='cargar_noticia'),
    
]
