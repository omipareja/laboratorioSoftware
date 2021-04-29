import smtplib
import uuid

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy,reverse
from django.contrib.auth import authenticate,login,logout
from django.template.loader import render_to_string
from .mixins import *
from library import settings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.views.generic import CreateView, FormView, TemplateView, UpdateView, ListView, DeleteView
#managers
from .models import User as usuario
from .forms import *


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

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('users:prueba'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password1']
        )

        login(self.request,user)
        return super(LoginUser,self).form_valid(form)

class Prueba(LoginRequiredMixin,TemplateView):
    template_name = 'prueba.html'

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('users:login')
        )

class RecuperarContraseña(FormView):
    template_name = 'ResetPassword.html'
    form_class = ResetPassword
    success_url = reverse_lazy('users:login')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def send_email_reset_password(self,user):

        try:
            #obtenemos la url correspondiente
            url = settings.DOMAIN if  not settings.DEBUG else self.request.META['HTTP_HOST']#si no esta en producion utilice el request

            user.token =  uuid.uuid4()
            user.save()

            mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            print(mailServer.ehlo())
            mailServer.starttls()
            print(mailServer.ehlo())
            mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            print('Conectado.....')

            # construimos el mensaje
            mensaje = MIMEMultipart()
            mensaje['From'] = settings.EMAIL_HOST_USER
            mensaje['To'] = user.email
            mensaje['subject'] = 'Recuperacion de contraseña'

            content = render_to_string('send_email.html', {
                'user': user,
                'link_resetpwd': 'http://{}/cambiar-contraseña/{}'.format(url,str(user.token)),
                'link_home': 'http://{}/login/'.format(url),

            })

            mensaje.attach(MIMEText(content, 'html'))

            mailServer.sendmail(settings.EMAIL_HOST_USER, user.email, mensaje.as_string())
            print('correo enviado...')
        except Exception as e:
            print(e)

    def form_valid(self, form):
        user = form.get_user()
        print(self.request.META['HTTP_HOST'])
        self.send_email_reset_password(user=user)
        return HttpResponseRedirect(self.success_url)

class CambiarContraseña(FormView):
    form_class = ChangePassword
    template_name = 'cambiarcontraseña.html'
    success_url = reverse_lazy('users:login')

    def get(self,request,*args,**kwargs):#revisar si el link existe
        token = self.kwargs['token']
        if usuario.objects.filter(token=token).exists(): #si existe un usuario con este token se le actualiza la contraseña
            return super().get(request, *args, **kwargs)
        else:
            print('no existe')
            return HttpResponseRedirect('/')


    def form_valid(self, form):
        user = usuario.objects.get(token=self.kwargs['token'])
        user.set_password(form.cleaned_data['password1'])
        user.token = uuid.uuid4()
        user.save()

        return super(CambiarContraseña, self).form_valid(form)

class UpdateUsuario(LoginRequiredMixin,UpdateView):
    model = usuario
    template_name = 'UpdateUser.html'
    form_class = UpdateUserForm
    success_url = reverse_lazy('pruebas:prueba')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args,**kwargs)
    def get_object(self, queryset=None):#sirve para hacer el update del usuario con el que estamos logueado
        return self.request.user

class ReclutarAdministrador(LoginRequiredMixin,FormView):
    template_name = 'reclutar_admin.com.html'
    form_class = ReclutarAdminForm
    success_url = reverse_lazy('users:login')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def send_email_reset_password(self,user,email):

        try:
            #obtenemos la url correspondiente
            url = settings.DOMAIN if  not settings.DEBUG else self.request.META['HTTP_HOST']#si no esta en producion utilice el request


            user.token =  uuid.uuid4()
            user.save()

            mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            print(mailServer.ehlo())
            mailServer.starttls()
            print(mailServer.ehlo())
            mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            print('Conectado.....')

            # construimos el mensaje
            mensaje = MIMEMultipart()
            mensaje['From'] = settings.EMAIL_HOST_USER
            mensaje['To'] = email
            mensaje['subject'] = 'Nuevo administrador'

            content = render_to_string('send_admin.html', {
                'user': 'Nuevo Tripulante',
                'link_resetpwd': 'http://{}/crear-administrador/{}'.format(url,str(user.token)),
                'link_home':'http://{}/login/'.format(url),

            })

            mensaje.attach(MIMEText(content, 'html'))

            mailServer.sendmail(settings.EMAIL_HOST_USER, email, mensaje.as_string())
            print('correo enviado...')
        except Exception as e:
            print(e)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = self.request.user
        self.send_email_reset_password(user,email)
        return super(ReclutarAdministrador, self).form_valid(form)

class NewAdmin(FormView):

    template_name = 'nuevo_admin.html'
    form_class = AdminRegisterForm
    success_url = reverse_lazy('users:login')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):  # revisar si el link existe
        token = self.kwargs['token']
        if usuario.objects.filter(
                token=token).exists():  # si existe un usuario con este token se le actualiza la contraseña
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')

    def form_valid(self, form):

        user = usuario.objects.create_admin(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
            lugar_nacimiento=form.cleaned_data['lugar_nacimiento'],
            dni=form.cleaned_data['dni'],
            avatar=form.cleaned_data['avatar']
        )
        # usuario.objects.create(form.cleaned_data('categoria'))

        codigo = self.kwargs['token']
        admin = usuario.objects.get(token=codigo)
        admin.token = uuid.uuid4()
        admin.save()
        return super(NewAdmin, self).form_valid(form)

class ListAdminView(LoginRequiredMixin,ValidatePermissionRequiredMixin,ListView):
    model = usuario
    template_name = 'list_admin.html'
    context_object_name = 'admin'
    permission_required = 'view_user'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        #grupo = self.request.user.groups.all()[0]
        #print('grupos',grupo.permissions.filter(codename=self.))
        list = usuario.objects.filter(nivel_accesibilidad=2)
        return  list

class DeleteAdmin(LoginRequiredMixin,DeleteView):
    model = usuario
    template_name = "delete_admin.html"
    success_url = reverse_lazy('users:listar-admin')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

class Test(TemplateView):
    template_name = 'send_email.html'
