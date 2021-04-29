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
    path('reseteo-contraseña/',RecuperarContraseña.as_view(),name='reset-password'),
    path('cambiar-contraseña/<str:token>/',CambiarContraseña.as_view(),name='change-password'),
    path('actualizar-usuario/',UpdateUsuario.as_view(),name='update-user'),
    path('añadir-administrador/',ReclutarAdministrador.as_view(),name='añadir-admin'),
    path('crear-administrador/<str:token>/',NewAdmin.as_view(),name='crear-admin'),
    path('listar-administrador/',ListAdminView.as_view(),name='listar-admin'),
    path('eliminar-administrador/<int:pk>/',DeleteAdmin.as_view(),name='eliminar-admin'),

]