from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from .forms import Createlibro
#Modelos
from .models import *
# Create your views here.
class NuevoLibroCreateView(CreateView):
    template_name = 'nuevo_libro.html'
    model = Libro
    form_class = Createlibro
    success_url = reverse_lazy('libros:list_libro')


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class ListarLibro(ListView):
    template_name = 'lista_libros.html'
    context_object_name = 'libros'
    model = Libro
    paginate_by = 8

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class EditarLibro(UpdateView):
    template_name = 'editar_libro.html'
    form_class = Createlibro
    model = Libro
    success_url = reverse_lazy('libros:list_libro')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class EliminarLibro(DeleteView):
    template_name = 'eliminar_libro.html'
    model = Libro
    success_url = reverse_lazy('libros:list_libro')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class BusquedaLibros(ListView):
    template_name = 'busqueda_libros.html'
    context_object_name = 'libros'
    #paginate_by = 8

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        select = self.request.GET.get('select', '')
        print(select)
        resultado = Libro.objects.buscar_libro(kword,select)
        return resultado