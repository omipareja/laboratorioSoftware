from django.db import models
from .choices import ESTADO_LIBRO
from .managers import LibroManager
# Create your models here.
class Category(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    isbn = models.TextField(unique=True)
    autor = models.TextField(max_length=30)
    titulo = models.TextField(max_length=50,blank=True,null=True)
    categoria = models.ManyToManyField(Category)
    numero_paginas = models.IntegerField()
    editorial = models.TextField(max_length=50)
    fecha_publicacion = models.DateField(blank=True,null=True)
    idioma = models.TextField()
    estado = models.CharField(max_length=15,choices=ESTADO_LIBRO,default='nuevo')
    precio = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    portada = models.ImageField(upload_to='portadas',blank=True,null=True)


    objects = LibroManager()



    def __str__(self):
        return self.titulo