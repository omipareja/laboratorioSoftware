from django.shortcuts import redirect
from datetime import datetime
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from crum import  get_current_request #me permite trabajar con la session actual
from django.contrib.auth.models import Group

#se implementan grupos
class ValidatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

#
#     def get_perms(self): #obtiene un arreglo con los permisos
#         perms = []
#         if isinstance(self.permission_required, str):
#             perms.append(self.permission_required)
#         else:
#             perms = list( self.permission_required)
#         return perms
#

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('pruebas:prueba')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.groups.all()[0]:
            group = self.request.user.groups.all()[0]
            if  group.permissions.filter(codename=self.permission_required): #estoy preguntando si ese grupo no tiene los permisos adociados
                return super().dispatch(request, *args, **kwargs)
        messages.error(self.request, 'No tiene permiso para ingresar a este módulo')
        return HttpResponseRedirect(self.get_url_redirect())




#esta clase es para validar los permisos sin losgrupos
# class ValidatePermissionRequiredMixin(object):
#     permission_required = ''
#     url_redirect = None
#
#     def get_perms(self):
#         if isinstance(self.permission_required, str):
#             perms = (self.permission_required,)
#         else:
#             perms = self.permission_required
#         return perms
#
#     def get_url_redirect(self):
#         if self.url_redirect is None:
#             return reverse_lazy('index')
#         return self.url_redirect
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.has_perms(self.get_perms()):
#             return super().dispatch(request, *args, **kwargs)
#         messages.error(request, 'No tiene permiso para ingresar a este módulo')
#         return HttpResponseRedirect(self.get_url_redirect())
