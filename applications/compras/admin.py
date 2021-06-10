from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Compras)
admin.site.register(DetalleCompra)
admin.site.register(Carrito)
admin.site.register(DevolucionProducto)
admin.site.register(Reservas)