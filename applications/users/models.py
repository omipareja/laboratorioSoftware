from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager
from applications.libros.models import Category
from .choices import MUNICIPIOS_COLOMBIA
class User(AbstractBaseUser,PermissionsMixin):

    username = models.CharField(max_length=16,unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30,blank=True,null=True)
    apellidos = models.CharField(max_length=30,blank=True,null=True)
    fecha_nacimiento = models.DateField(blank=True,null=True)
    lugar_nacimiento = models.CharField(max_length=60,choices=MUNICIPIOS_COLOMBIA,default='Pereira',blank=True,null=True)
    dni = models.IntegerField(blank=True,null=True)
    categoria = models.ManyToManyField(Category,blank=True)
    avatar = models.ImageField(upload_to='avatares',blank=True,null=True)
    nivel_accesibilidad = models.IntegerField()
    #propios de Abstrac
    is_staff = models.BooleanField(default=False)



    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos