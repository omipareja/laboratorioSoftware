from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView,ListView,DeleteView,FormView,UpdateView
from .models import Tarjeta
from .forms import CrearTarjetaForm,ActualizarTarjetaForm
# Create your views here.

class CrearTarjeta(FormView):
    template_name = 'add_tarjeta.html'
    model = Tarjeta
    form_class = CrearTarjetaForm
    success_url = reverse_lazy('home:index')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        numero = form.cleaned_data['numero']
        fecha = form.cleaned_data['fecha_vencimiento']
        cvv = form.cleaned_data['cvv']
        saldo = form.cleaned_data['saldo']

        tarjeta = Tarjeta.objects.create(
            numero= numero,
            fecha_vencimiento= fecha,
            cvv = cvv,
            usuario= self.request.user,
            saldo = saldo
        )
        tarjeta.save()
        return super(CrearTarjeta, self).form_valid(form)

class ListarTarjeta(ListView):
    template_name = 'listar_tarjeta.html'
    model = Tarjeta
    context_object_name = 'tarjetas'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Tarjeta.objects.filter(
            usuario= self.request.user
        )

class EliminarTarjeta(DeleteView):
    template_name = 'eliminar_tarjeta.html'
    model = Tarjeta
    success_url = reverse_lazy('tarjetas:list_tarjeta')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class AumentarSaldo(UpdateView):
    template_name = 'aumentar_saldo.html'
    model = Tarjeta
    success_url = reverse_lazy('tarjetas:list_tarjeta')
    form_class = ActualizarTarjetaForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)