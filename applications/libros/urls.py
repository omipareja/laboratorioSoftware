from django.test import TestCase
from django.urls import path
from applications.libros.views import *
# Create your tests here.

app_name = 'libros'

urlpatterns = [
    ################################urls_administracion##########################3
    path('nuevo_libro/',NuevoLibroCreateView.as_view(),name='add_libro'),
    path('listar_libro/',ListarLibro.as_view(),name='list_libro'),
    path('editar_libro/<int:pk>/',EditarLibro.as_view(),name='update_libro'),
    path('eliminar_libro/<int:pk>/',EliminarLibro.as_view(),name='eliminar_libro'),
    ##################################urls_usuarios##################################
    path('buscar_libro/',BusquedaLibros.as_view(),name='buscar_libro'),
    path('crear_categoria/',CrearCateoria.as_view(),name='crear_categoria'),
    path('listar_libro_cliente/',ListarLibroCliente.as_view(),name='libro_cliente'),
    path('detalle_libros/<int:pk>/',Detallelibros.as_view(),name='detalle_libro'),
]