from django.test import TestCase
from django.urls import path
from applications.prueba.views import *
# Create your tests here.

app_name = 'pruebas'

urlpatterns = [
    path('prueba/',PruebaIndex.as_view(),name='prueba'),
    #path('Registro/',Registro.as_view(),name='prueba'),
]