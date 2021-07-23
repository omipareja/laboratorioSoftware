from django.db import models
from applications.users.models import User
from .choices import franquicias
# Create your models here.

class Tarjeta(models.Model):
    franquicia = models.CharField(max_length=60,choices=franquicias,default='VISA')
    numero = models.CharField(max_length=20,unique=True)
    fecha_vencimiento = models.DateField()
    cvv = models.TextField()
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    saldo = models.FloatField(default=0,blank=True,null=True)



    def __str__(self):
        return str(self.numero)