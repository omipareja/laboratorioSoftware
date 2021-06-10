from django.db import models
'''Creditos a: Code With Tomi  
   Nombre video:How To Build A Realtime Chat App With Django
   video:https://www.youtube.com/watch?v=IpAk1Eu52GU
   Repositorio github:https://github.com/tomitokko/django-chat-app
   Implemntado por:Juan Manuel Sanchez Pareja
 '''
'''Librerias'''
# Create your models here.
from datetime import datetime
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)