from django.test import TestCase
from django.urls import path
from applications.compras.views import *
# Create your tests here.

app_name = 'compras'

urlpatterns = [
    path('pruebita/',PrueabaPost.as_view(),name='pruebita'),
    path('listar_compras/',ListarCompras.as_view(),name='listar_compras'),
]