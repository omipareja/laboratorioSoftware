from django.db import models

#Modelos llaves foraneas
from applications.users.models import User
from applications.libros.models import Libro
# Create your models here.

Estados = (
    ('reservado','reservado'),
    ('cancelado','cancelado'),
)

class Reservas(models.Model):

    usuario = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    estado = models.CharField(max_length=11,choices=Estados,default='reservado',blank=True,null=True)
    libros = models.ManyToManyField(Libro)
    fecha = models.DateField(blank=True,null=True)
    cantidad = models.PositiveIntegerField(blank=True,null=True)
    def __str__(self):
        return str(self.usuario) + '-' + str(self.estado)