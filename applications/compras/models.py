from django.db import models
from model_utils.models import TimeStampedModel
from datetime import date
from django.utils import timezone
#modelos llaves foraneas
from  applications.users.models import User
from applications.libros.models import Libro
from  applications.tarjetas.models import Tarjeta

#Managers
from .managers import *
# Create your models here.
class Compras(TimeStampedModel):
    fecha_compra = models.DateField()
    cantidad = models.PositiveIntegerField('Cantidad Productos',blank=True,null=True)
    monto = models.DecimalField('Monto',default=0.00, max_digits=9,decimal_places=3,blank=True)
    cancelado = models.CharField(max_length=30,default='Aprobada',blank=True)
    cliente = models.ForeignKey(User,on_delete=models.PROTECT, blank=True, null=True)
    tarjeta = models.ForeignKey(Tarjeta,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.cliente.nombres) + '-' + str(self.fecha_compra)

class DetalleCompra(TimeStampedModel):
    compras = models.ForeignKey(Compras,on_delete=models.PROTECT,related_name='compra_detalle')
    producto = models.ForeignKey(Libro,on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=0)
    precio_compra = models.DecimalField(max_digits=10,decimal_places=3,blank=True,null=True)

    def __str__(self):
        return str(self.compras.pk) + '-' + str(self.producto.titulo)

class Carrito(TimeStampedModel):
    codigo = models.CharField(max_length=15,null=True,blank=True)
    productos = models.ForeignKey(Libro,on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    objects = CarroComprasManager()
    class Meta:
        ordering=['-created']

    def __str__(self):
        return str(self.productos.titulo)

class DevolucionProducto(TimeStampedModel):
    cliente = models.ForeignKey(User,on_delete=models.CASCADE)
    producto = models.ForeignKey(Libro,on_delete=models.CASCADE)
    factura = models.ForeignKey(Compras,on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=1000)
    fecha_devolucion = models.DateField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return str(self.fecha_devolucion)+'-'+str(self.producto.titulo)

class  Reservas(TimeStampedModel):
    codigo = models.CharField(max_length=15,null=True,blank=True)
    productos = models.ForeignKey(Libro,on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    objects = ReservasManager()

    objects = CarroComprasManager()
    class Meta:
        ordering=['-created']

    def __str__(self):
        return str(self.productos.titulo)