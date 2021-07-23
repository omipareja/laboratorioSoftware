from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.utils.decorators import method_decorator
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView,ListView,View
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
# Create your views here.
from .forms import PruebaForm,MetodoPago,DevolucionForm
from .models import *
from  applications.libros.models import Libro
from  applications.tarjetas.models import Tarjeta
from  .models import DevolucionProducto
from .functions import *
#Compras
class ListarCompras(ListView):
    template_name = 'listar_compras.html'
    model = Compras
    context_object_name = 'compras'
    
    def get_queryset(self):
        print(self.request.user.nombres)
        return Compras.objects.filter(
            cliente = self.request.user
        ).order_by('-created')[:4]

class AñadirCarrito(View):
    ''' Añade el producto selecionado al carro de compras '''

    def post(self,request,*args,**kwargs):
        usuario = request.user
        producto = kwargs['pk']
        count = 1

        obj, created = Carrito.objects.get_or_create(
            codigo = str(producto)+'-'+str(usuario),
            defaults={
                'productos': Libro.objects.get(pk = producto),
                'cantidad': count,
                'user':usuario

            }
        )

        if not created:
            obj.cantidad = obj.cantidad + count
            obj.save()
        return HttpResponseRedirect(reverse('libros:libro_cliente'))

class CarroCompraView(FormView):
    template_name = 'carro_compras.html'
    form_class = MetodoPago
    success_url = '.'

    def form_valid(self, form):
        tarjeta = form.cleaned_data['metodo']
        usuario = self.request.user
        tar2 = 0
        tar = Tarjeta.objects.filter(numero=tarjeta,usuario=usuario).exists()
        if tar == True:
            tar2 = Tarjeta.objects.get(numero=tarjeta,usuario=usuario)
        if tar == False:
            messages.error(self.request, 'Tarjeta invalida, no coincide con ninguna de las registradas. Por favor verifica e intentalo de nuevo.')
            return HttpResponseRedirect(reverse('compras:mostrar_carro'))
        total_cobrar = int(Carrito.objects.total_cobrar(self.request.user))
        saldo_tarjeta = tar2.saldo
        if tar == True:
            if saldo_tarjeta >= total_cobrar:
                '''Logica para hacer el pago'''
                procesar_venta(self,usuario=usuario,total_cobrar=total_cobrar,tarjeta=tar2)

            else:
                messages.error(self.request, 'No tienes suficiente saldo')
                return HttpResponseRedirect(reverse('compras:mostrar_carro'))

        return super(CarroCompraView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos']= Carrito.objects.filter(user = self.request.user)
        context["total"] = Carrito.objects.total_cobrar(self.request.user)
        context['tarjetas'] = User.objects.filter(pk=self.request.user.pk)
        return context

class RestarProducto(View):
    def post(self,request,*args,**kwargs):
        pk = self.kwargs['pk']
        car = Carrito.objects.get(pk=pk)

        if car.cantidad > 1:
            car.cantidad = car.cantidad -1
            car.save()

        return  HttpResponseRedirect(reverse('compras:mostrar_carro'))

class SumarProducto(View):
    def post(self,request,*args,**kwargs):
        pk = self.kwargs['pk']
        car = Carrito.objects.get(pk=pk)

        if car.cantidad  < car.productos.stock:
            car.cantidad = car.cantidad +1
            car.save()

        return  HttpResponseRedirect(reverse('compras:mostrar_carro'))

class EliminarProducto(View):
    def post(self,request,*args,**kwargs):
        pk= self.kwargs['pk']
        car = Carrito.objects.get(pk=pk)
        car.delete()
        return  HttpResponseRedirect(reverse('compras:mostrar_carro'))

class VaciarCarro(View):

    def post(self,request,*args,**kwargs):
        Carrito.objects.filter(user=self.request.user).delete()
        return HttpResponseRedirect(reverse('compras:mostrar_carro'))

class CancelarCompraView(View):

    def post(self,request,*args,**kwargs):
        pk = self.kwargs['pk']
        usuario = self.request.user
        compra = Compras.objects.get(pk=pk)
        compra.cancelado = 'Cancelado'
        compra.save()

        compra.tarjeta.saldo = float(compra.tarjeta.saldo) + float(compra.monto)
        compra.tarjeta.save()

        productos = compra.compra_detalle.all()

        for p in productos:
            print(p.producto.stock)
            p.producto.stock = p.producto.stock + p.cantidad
            print(p.producto.stock)
            p.producto.save()


        return HttpResponseRedirect(reverse('compras:listar_compras'))
#Devoluciones
class DevolucionCompraView(FormView):
    template_name = 'crear_devolucion.html'
    form_class =  DevolucionForm
    success_url = reverse_lazy('compras:listar_compras')

    def form_valid(self, form):
        descripcion = form.cleaned_data['descripcion']
        user = self.request.user
        producto_detalle = DetalleCompra.objects.get( pk =self.kwargs['pk'])


        devolucion = DevolucionProducto.objects.create(
            cliente=user,
            producto = producto_detalle.producto,
            factura= producto_detalle.compras,
            descripcion = descripcion,
            fecha_devolucion= timezone.now(),
            estado= 'Devolucion'

        )
        devolucion.save()

        compra = producto_detalle.compras
        compra.cancelado = 'Devolucion'
        compra.save()
        return HttpResponseRedirect(reverse('compras:listar_compras'))

class ListarDevolucionesUsuario(ListView):
    template_name = 'listar_devoluciones.html'
    context_object_name = 'devoluciones'

    def get_queryset(self):
        consulta = DevolucionProducto.objects.filter(estado='Devolucion',cliente=self.request.user )
        return consulta

#Reservas
class AñadirReserva(View):
    ''' Añade el producto selecionado al carro de compras '''

    def post(self,request,*args,**kwargs):
        usuario = request.user
        producto = kwargs['pk']
        count = 1

        obj, created = Reservas.objects.get_or_create(
            codigo = str(producto)+'-'+str(usuario),
            defaults={
                'productos': Libro.objects.get(pk = producto),
                'cantidad': count,
                'user':usuario

            }
        )

        if not created:
            obj.productos.stock = obj.productos.stock - 1
            obj.productos.save()
            obj.cantidad = obj.cantidad + count
            obj.save()




        return HttpResponseRedirect(reverse('libros:libro_cliente'))

class ListarReserva(FormView):
    template_name = 'listar_reserva.html'
    form_class = MetodoPago
    success_url = '.'

    def form_valid(self, form):
        tarjeta = form.cleaned_data['metodo']
        usuario = self.request.user
        tar2 = 0
        tar = Tarjeta.objects.filter(numero=tarjeta,usuario=usuario).exists()
        if tar == True:
            tar2 = Tarjeta.objects.get(numero=tarjeta,usuario=usuario)
        if tar == False:
            messages.error(self.request, 'Tarjeta invalida,no coincide con las registradas')
            return HttpResponseRedirect(reverse('compras:listar_reserva'))
        total_cobrar = int(Carrito.objects.total_cobrar(self.request.user))
        saldo_tarjeta = tar2.saldo
        if tar == True:
            if saldo_tarjeta >= total_cobrar:
                '''Logica para hacer el pago'''
                procesar_venta_reserva(self,usuario=usuario,total_cobrar=total_cobrar,tarjeta=tar2)

            else:
                messages.error(self.request, 'Saldo insuficiente')
                return HttpResponseRedirect(reverse('compras:listar_reserva'))

        return super(ListarReserva, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservas'] = Reservas.objects.filter(user=self.request.user)
        context['total'] = Reservas.objects.total_cobrar(self.request.user)
        return context

class SumarProsuctoReserva(View):
    def post(self,request,*args,**kwargs):
        pk = self.kwargs['pk']
        car = Reservas.objects.get(pk=pk)

        if car.cantidad  < car.productos.stock:
            car.cantidad = car.cantidad +1
            car.save()

        car.productos.stock = car.productos.stock - 1
        car.productos.save()

        return  HttpResponseRedirect(reverse('compras:listar_reserva'))

class RestarProductoReservas(View):
    def post(self,request,*args,**kwargs):
        pk = self.kwargs['pk']
        car = Reservas.objects.get(pk=pk)

        if car.cantidad > 1:
            car.cantidad = car.cantidad -1
            car.save()

        car.productos.stock = car.productos.stock + 1
        car.productos.save()

        return  HttpResponseRedirect(reverse('compras:listar_reserva'))

class EliminarProductoReservas(View):
    def post(self,request,*args,**kwargs):
        pk= self.kwargs['pk']
        car = Reservas.objects.get(pk=pk)
        car.delete()

        car.productos.stock = car.productos.stock + car.cantidad
        car.productos.save()

        return  HttpResponseRedirect(reverse('compras:listar_reserva'))

