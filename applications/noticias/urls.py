from django.test import TestCase
from django.urls import path
from .views import *
# Create your tests here.

app_name = 'noticias'

urlpatterns = [
    ###########################urls_para_Adiministradores####################################
    path('crear_noticia/',CrearNoticiaView.as_view(),name='crear_noticia'),
    path('noticias/',ListarNoticiaView.as_view(),name='listar_noticia'),
    path('eliminar_noticia/<int:pk>/',DeleteNoticiaView.as_view(),name='eliminar_noticia'),
    path('actualizar_noticia/<int:pk>/',UpdateNoticia.as_view(),name='actualizar_noticia'),
    ###########################3urls_usuario###############################################33
    path('mostrar_noticia/',ListarNoticiaUsuario.as_view(),name='mostrar_noticia'),
    path('detalle_noticia/<int:pk>/',DetalleNoticiaUsuario.as_view(),name='detalle_noticia'),

]