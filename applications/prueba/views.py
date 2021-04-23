from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class PruebaIndex(TemplateView):
    template_name = 'index.html'

class Registro(TemplateView):
    template_name = 'registro.html'