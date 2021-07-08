from django.test import TestCase
from django.urls import path
from applications.tarjetas.views import *
# Create your tests here.

app_name = 'tarjetas'

urlpatterns = [
    path('nuevaTarjeta/',CrearTarjeta.as_view(),name='add_tarjeta'),
    path('misTarjetas/',ListarTarjeta.as_view(),name='list_tarjeta'),
    path('eliminarTarjeta/<int:pk>/',EliminarTarjeta.as_view(),name='eliminar_tarjeta'),
    path('aumentarSaldo/<int:pk>/',AumentarSaldo.as_view(),name='aumentar_Saldo'),
]