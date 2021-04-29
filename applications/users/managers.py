from django.db import models

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager,models.Manager):

    def _create_user(self,username,email,nivel_accesibilidad,password,is_staff,is_superuser,**extra_fields):
        user = self.model(
            username = username,
            email = email,
            nivel_accesibilidad = nivel_accesibilidad,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,username,email,password=None,**extra_fields):
        return self._create_user(username,email,1,password,False,False,**extra_fields)

    def create_admin(self,username,email,password=None,**extra_fields):
        return self._create_user(username,email,2,password,False,False,**extra_fields)


    def create_superuser(self,username,email,nivel_accesibilidad=3,password=None,**extra_fields):
        return  self._create_user(username,email,nivel_accesibilidad,password,True,True,**extra_fields)