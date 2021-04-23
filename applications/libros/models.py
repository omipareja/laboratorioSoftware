from django.db import models

# Create your models here.
class Category(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre
