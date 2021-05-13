from django.test import TestCase
from django.urls import path
from applications.tarjetas.views import *
# Create your tests here.

app_name = 'tarjetas'

urlpatterns = [
    path('nueva_tarjeta/',CrearTarjeta.as_view(),name='add_tarjeta'),
    path('listar_tarjeta/',ListarTarjeta.as_view(),name='list_tarjeta'),
    path('eliminar_tarjeta/<int:pk>/',EliminarTarjeta.as_view(),name='eliminar_tarjeta'),
    path('aumentar_saldo/<int:pk>/',AumentarSaldo.as_view(),name='aumentar_Saldo'),
]