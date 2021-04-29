from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class PruebaIndex(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'

class Registro(TemplateView):
    template_name = 'registro.html'