from django.db import models
from model_utils.models import TimeStampedModel

from applications.users.models import User

class Noticias(TimeStampedModel):
    titulo = models.CharField(max_length=60)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    genero = models.CharField(max_length=30)
    idioma = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=1000)
    imagen = models.ImageField(upload_to='Noticias',blank=True,null=True)

    def __str__(self):
        return self.titulo