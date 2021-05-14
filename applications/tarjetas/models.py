from django.db import models
from applications.users.models import User
# Create your models here.

class Tarjeta(models.Model):
    numero = models.IntegerField(unique=True)
    fecha_vencimiento = models.DateField()
    cvv = models.TextField()
    usuario = models.ForeignKey(User,on_delete=models.PROTECT,blank=True,null=True)
    saldo = models.FloatField(default=0,blank=True,null=True)



    def __str__(self):
        return str(self.numero)