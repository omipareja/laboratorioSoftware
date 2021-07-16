from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
from .models import Noticias
from .forms import CrearNoticiaForm
# Create your views here.

class CrearNoticiaView(CreateView):
    template_name = 'crear_noticias.html'
    model = Noticias
    form_class = CrearNoticiaForm
    success_url =  reverse_lazy('noticias:listar_noticia')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        noticia = form.save(commit=False)
        noticia.autor = self.request.user
        noticia.save()
        return super(CrearNoticiaView, self).form_valid(form)

class ListarNoticiaView(ListView):
    template_name = 'listar_noticias.html'
    model = Noticias
    context_object_name = 'noticias'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class DeleteNoticiaView(DeleteView):
    template_name = 'borrar_noticias.html'
    model = Noticias
    success_url = reverse_lazy('noticias:listar_noticia')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class UpdateNoticia(UpdateView):
    template_name = 'actualizar_noticia.html'
    model = Noticias
    form_class = CrearNoticiaForm
    success_url = reverse_lazy('noticias:listar_noticia')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class ListarNoticiaUsuario(ListView):
    template_name = 'noticia_usuario.html'
    model = Noticias
    context_object_name = 'noticias'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class DetalleNoticiaUsuario(DetailView):
    template_name = 'detalle_noticia.html'
    model = Noticias
    context_object_name = 'noticias'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
