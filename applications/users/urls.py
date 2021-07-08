from django.test import TestCase
from django.urls import path
from applications.users.views import *
# Create your tests here.

app_name = 'users'

urlpatterns = [
    path('registro/',UserRegisterView.as_view(),name='registro'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('recuperarContrasena/',RecuperarContraseña.as_view(),name='reset-password'),
    path('cambiarContrasena/<str:token>/',CambiarContraseña.as_view(),name='change-password'),
    path('editarPerfil/',UpdateUsuario.as_view(),name='update-user'),
    path('invitarAdmin/',ReclutarAdministrador.as_view(),name='añadir-admin'),
    path('crearAdmin/<str:token>/',NewAdmin.as_view(),name='crear-admin'),
    path('administradores/',ListAdminView.as_view(),name='listar-admin'),
    path('eliminarAdmin/<int:pk>/',DeleteAdmin.as_view(),name='eliminar-admin'),
    path('convertirUsuario',TemplateAdmin.as_view(),name='convertir-admin'),

]