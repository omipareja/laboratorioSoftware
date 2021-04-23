from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy,reverse
from django.contrib.auth import authenticate,login,logout

from django.views.generic import CreateView,FormView,TemplateView
#managers
from .models import User
from .forms import UserRegisterForm,LoginForm

class UserRegisterView(FormView):
    template_name = 'registro.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    def form_valid(self, form):
        @method_decorator(csrf_exempt)
        def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)

        usuario =User.objects.create_user(
            username = form.cleaned_data['username'],
            email = form.cleaned_data['email'],
            password= form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento'],
            lugar_nacimiento = form.cleaned_data['lugar_nacimiento'],
            dni = form.cleaned_data['dni'],
            avatar = form.cleaned_data['avatar']
        )
        usuario.categoria.set = form.cleaned_data['categoria']
        usuario.save()
        #usuario.objects.create(form.cleaned_data('categoria'))
        return super(UserRegisterView,self).form_valid(form)

class LoginUser(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('users:prueba')

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password1']
        )

        login(self.request,user)
        return super(LoginUser,self).form_valid(form)

class Prueba(TemplateView):
    template_name = 'prueba.html'

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('users:login')
        )
