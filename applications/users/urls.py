from django.test import TestCase
from django.urls import path
from applications.users.views import *
# Create your tests here.

app_name = 'users'

urlpatterns = [
    path('registro/',UserRegisterView.as_view(),name='registro'),
    path('login/',LoginUser.as_view(),name='login'),
    path('pruebas/',Prueba.as_view(),name='prueba'),
    path('logout/',LogoutView.as_view(),name='logout'),

]