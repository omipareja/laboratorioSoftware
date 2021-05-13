from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView,ListView
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
# Create your views here.
from .forms import PruebaForm
from .models import Compras
class PrueabaPost(FormView):
    template_name = 'prueba_post.html'
    form_class = PruebaForm
    success_url = reverse_lazy('compras:pruebita')
    guardar = []
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        prueba = request.POST['prueba']
        self.guardar.append(prueba)
        print(self.guardar)
        return HttpResponseRedirect(reverse_lazy('compras:pruebita'))

class ListarCompras(ListView):
    template_name = 'listar_compras.html'
    model =Compras
    context_object_name = 'compras'
    
    def get_queryset(self):
        print(self.request.user.nombres)
        return Compras.objects.filter(
            cliente = self.request.user
        )