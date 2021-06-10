from django.test import TestCase
from django.urls import path
from applications.compras.views import *
# Create your tests here.

app_name = 'compras'

urlpatterns = [
    path('listar_compras/',ListarCompras.as_view(),name='listar_compras'),
    path('añadir_carro/<int:pk>/', AñadirCarrito.as_view(), name='añadir_carro'),
    path('mostrar_carro/', CarroCompraView.as_view(), name='mostrar_carro'),
    path('restar_carro/<int:pk>', RestarProducto.as_view(), name='restar_producto'),
    path('sumar_carro/<int:pk>', SumarProducto.as_view(), name='sumar_producto'),
    path('eliminar_producto/<int:pk>', EliminarProducto.as_view(), name='eliminar_producto'),
    path('vaciar_carro/', VaciarCarro.as_view(), name='vaciar_carro'),
    path('cancelar_compra/<int:pk>/', CancelarCompraView.as_view(), name='cancelar_compra'),
    ###################Devoluciones#######################
    path('nueva_devolucion/<int:pk>/', DevolucionCompraView.as_view(), name='nueva_devolucion'),
    path('listar_devolucion/', ListarDevolucionesUsuario.as_view(), name='listar_devolucion'),
    #######################Reservas####################################3
    path('crear_reserva/<int:pk>/',AñadirReserva.as_view(),name = 'crear_reserva'),
    path('listar_reserva/',ListarReserva.as_view(),name = 'listar_reserva'),
    path('aumentar_reserva/<int:pk>',SumarProsuctoReserva.as_view(),name = 'aumentar_reserva'),
    path('disminuir_reserva/<int:pk>',RestarProductoReservas.as_view(),name = 'disminuir_reserva'),
    path('eliminar/productos/reservas/<int:pk>',EliminarProductoReservas.as_view(),name = 'eliminar_reserva'),

]