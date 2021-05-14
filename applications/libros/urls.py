from django.test import TestCase
from django.urls import path
from applications.libros.views import *
# Create your tests here.

app_name = 'libros'

urlpatterns = [
    path('nuevo_libro/',NuevoLibroCreateView.as_view(),name='add_libro'),
    path('listar_libro/',ListarLibro.as_view(),name='list_libro'),
    path('editar_libro/<int:pk>/',EditarLibro.as_view(),name='update_libro'),
    path('eliminar_libro/<int:pk>/',EliminarLibro.as_view(),name='eliminar_libro'),
]