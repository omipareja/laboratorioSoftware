from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currentUrl'] = 'inicio'
        return context

class noticias(TemplateView):
    template_name = 'noticias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currentUrl'] = 'noticias'
        return context

class contacto(TemplateView):
    template_name = 'contacto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currentUrl'] = 'contacto'
        return context