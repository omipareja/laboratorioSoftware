from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,View
from .forms import Createlibro,CreateCategoryForm
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
    template_name = 'lista_libros_admin.html'
    context_object_name = 'libros'
    model = Libro
    paginate_by = 4

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class ListarLibroCliente(ListView):
    template_name = 'listar_libros_cliente.html'
    context_object_name = 'libros'
    paginate_by = 10

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        select = self.request.GET.get('select', '')
        if select:
            categoria = Category.objects.get(nombre=select)
            resultado = Libro.objects.libros_category(categoria)
            return resultado
        else:
            resultado = Libro.objects.libros_clientes(select)
            return resultado


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Category.objects.all()
        return context

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

class CrearCateoria(CreateView):
    template_name = 'crear_categoria.html'
    model = Category
    form_class = CreateCategoryForm
    success_url = reverse_lazy('libros:list_libro')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class Detallelibros(DeleteView):
    template_name = 'detalle_libros.html'
    model = Libro

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

