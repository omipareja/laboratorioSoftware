from django.db.models import Prefetch
from applications.libros.models import Libro
from .models import *
from applications.tarjetas.models import Tarjeta

def procesar_venta(self,**params_venta):
    productos_en_carrito = Carrito.objects.filter(user=params_venta['usuario'])
    if productos_en_carrito.count() > 0:
        #se crea el objeto venta
        venta = Compras.objects.create(
            fecha_compra= timezone.now(),
            cantidad= 0,
            monto=0,
            cancelado='Aprobada',
            cliente= params_venta['usuario'],
            tarjeta=params_venta['tarjeta']
        )
        #
        ventas_detalle = []
        productos_en_veta = []
        for producto_car in productos_en_carrito:
            venta_detalle = DetalleCompra(
                compras = venta,
                producto= producto_car.productos,
                cantidad= producto_car.cantidad,
                precio_compra= producto_car.productos.precio
            )
            #Actualizamos el stock
            producto = producto_car.productos
            producto.stock = producto.stock - producto_car.cantidad
            #v
            ventas_detalle.append(venta_detalle)
            productos_en_veta.append(producto)

            venta.cantidad = venta.cantidad + producto_car.cantidad
            venta.monto = venta.monto + producto_car.cantidad * producto_car.productos.precio

        venta.save()
        DetalleCompra.objects.bulk_create(ventas_detalle)
        Libro.objects.bulk_update(productos_en_veta ,['stock'])
        productos_en_carrito.delete()

        restar_saldo = params_venta['tarjeta']
        restar_saldo.saldo = restar_saldo.saldo - params_venta['total_cobrar']
        restar_saldo.save()

        return  venta
    else:
        return None

def procesar_venta_reserva(self,**params_venta):
    productos_en_carrito = Reservas.objects.filter(user=params_venta['usuario'])
    if productos_en_carrito.count() > 0:
        #se crea el objeto venta
        venta = Compras.objects.create(
            fecha_compra= timezone.now(),
            cantidad= 0,
            monto=0,
            cancelado='Aprobada',
            cliente= params_venta['usuario'],
            tarjeta=params_venta['tarjeta']
        )
        #
        ventas_detalle = []
        productos_en_veta = []
        for producto_car in productos_en_carrito:
            venta_detalle = DetalleCompra(
                compras = venta,
                producto= producto_car.productos,
                cantidad= producto_car.cantidad,
                precio_compra= producto_car.productos.precio
            )
            #Actualizamos el stock
            producto = producto_car.productos
            producto.stock = producto.stock - producto_car.cantidad
            #v
            ventas_detalle.append(venta_detalle)
            productos_en_veta.append(producto)

            venta.cantidad = venta.cantidad + producto_car.cantidad
            venta.monto = venta.monto + producto_car.cantidad * producto_car.productos.precio

        venta.save()
        DetalleCompra.objects.bulk_create(ventas_detalle)
        Libro.objects.bulk_update(productos_en_veta ,['stock'])
        productos_en_carrito.delete()

        restar_saldo = params_venta['tarjeta']
        restar_saldo.saldo = restar_saldo.saldo - params_venta['total_cobrar']
        restar_saldo.save()

        return  venta
    else:
        return None
