from django.test import TestCase
from django.urls import path
from applications.compras.views import *
# Create your tests here.

app_name = 'compras'

urlpatterns = [
    path('compras/',ListarCompras.as_view(),name='listar_compras'),
    path('agregarAlCarrito/<int:pk>/', AñadirCarrito.as_view(), name='añadir_carro'),
    path('carrito/', CarroCompraView.as_view(), name='mostrar_carro'),
    path('restarCarro/<int:pk>', RestarProducto.as_view(), name='restar_producto'),
    path('sumarCarro/<int:pk>', SumarProducto.as_view(), name='sumar_producto'),
    path('eliminarProducto/<int:pk>', EliminarProducto.as_view(), name='eliminar_producto'),
    path('vaciarCarrito/', VaciarCarro.as_view(), name='vaciar_carro'),
    path('cancelarCompra/<int:pk>/', CancelarCompraView.as_view(), name='cancelar_compra'),
    ###################Devoluciones#######################
    path('crearDevolucion/<int:pk>/', DevolucionCompraView.as_view(), name='nueva_devolucion'),
    path('devoluciones/', ListarDevolucionesUsuario.as_view(), name='listar_devolucion'),
    #######################Reservas####################################3
    path('crearReserva/<int:pk>/',AñadirReserva.as_view(),name = 'crear_reserva'),
    path('reservas/',ListarReserva.as_view(),name = 'listar_reserva'),
    path('aumentarReserva/<int:pk>',SumarProsuctoReserva.as_view(),name = 'aumentar_reserva'),
    path('disminuirReserva/<int:pk>',RestarProductoReservas.as_view(),name = 'disminuir_reserva'),
    path('eliminarReservas/<int:pk>',EliminarProductoReservas.as_view(),name = 'eliminar_reserva'),

]