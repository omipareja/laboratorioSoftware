from django.db import models
from datetime import date
from django.utils import timezone
#modelos llaves foraneas
from  applications.users.models import User
from applications.libros.models import Libro
# Create your models here.
class Compras(models.Model):
    fecha_compra = models.DateField()
    cliente = models.ForeignKey(User,on_delete=models.PROTECT)
    total = models.DecimalField(default=0.00, max_digits=9,decimal_places=3)

    def __str__(self):
        return str(self.cliente.nombres) + '-' + str(self.fecha_compra)

class DetalleCompra(models.Model):
    compras = models.ForeignKey(Compras,on_delete=models.PROTECT,related_name='compra_detalle')
    producto = models.ForeignKey(Libro,on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=9,decimal_places=3)

    def __str__(self):
        return str(self.compras.pk) + '-' + str(self.producto.titulo)
