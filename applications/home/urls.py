from django.test import TestCase
from django.urls import path
from applications.home.views import *
# Create your tests here.

app_name = 'home'

urlpatterns = [
    path('', index.as_view(), name='index'),
]