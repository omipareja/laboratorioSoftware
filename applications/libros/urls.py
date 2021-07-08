from django.test import TestCase
from django.urls import path
from applications.libros.views import *
# Create your tests here.

app_name = 'libros'

urlpatterns = [
    ################################urls_administracion###########################
    path('agregarLibro/',NuevoLibroCreateView.as_view(),name='add_libro'),
    path('inventario/',ListarLibro.as_view(),name='list_libro'),
    path('editarLibro/<int:pk>/',EditarLibro.as_view(),name='update_libro'),
    path('eliminarLibro/<int:pk>/',EliminarLibro.as_view(),name='eliminar_libro'),
    ##################################urls_usuarios##################################
    path('buscarLibro/',BusquedaLibros.as_view(),name='buscar_libro'),
    path('crearCategoria/',CrearCateoria.as_view(),name='crear_categoria'),
    path('catalogo/',ListarLibroCliente.as_view(),name='catalogo'),
    path('detalles/<int:pk>/',Detallelibros.as_view(),name='detalle_libro'),
]