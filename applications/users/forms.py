from django import  forms
from .models import User
from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña',
                'class': 'form-control'
            }
        )
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir contraseña',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model=User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'fecha_nacimiento',
            'lugar_nacimiento',
            'dni',
            'categoria',
            'avatar'
        )
        widgets = {
            'username': forms.TextInput(

                attrs= {
                    'placeholder': 'Ingresa un nombre de usuario',
                    'class': 'form-control',
                    'required':'True'
                }
            ),
            'email': forms.TextInput(

                attrs={
                    'placeholder': 'Ingresa un correo electrónico',
                    'class': 'form-control',
                    'required': 'True'
                }
            ),
            'nombres': forms.TextInput(

                attrs={
                    'placeholder': 'Ingresa tu nombre',
                    'class': 'form-control',
                    'required': 'True'
                }
            ),
            'apellidos': forms.TextInput(

                attrs={
                    'placeholder': 'Ingresa tu apellido',
                    'class': 'form-control',
                    'required': 'True'
                }
            ),

            'lugar_nacimiento': forms.Select(

                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),

        }
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password1', forms.ValidationError('Las contraseñas no coinciden.'))
        if len(self.cleaned_data['password2']) < 8:
            self.add_error('password2', forms.ValidationError('La contraseña debe tener al menos 8 caracteres'))

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingresa tu nombre de usuario',
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingresa tu contraseña',
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        username =  self.cleaned_data['username']
        password = self.cleaned_data['password1']

        if not authenticate(username = username, password = password):
            self.add_error('password1', forms.ValidationError('Las credenciales no existen'))
        return  self.cleaned_data

class ResetPassword(forms.Form):
    username = forms.CharField(
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder':'Ingrese un username',
                'class': 'form-control',
                'autocomplete': 'off',
            }
        )
    )

    def clean(self):
        cleaned = super(ResetPassword,self).clean()
        if not  User.objects.filter(username = cleaned['username']).exists():
            self.add_error('username', forms.ValidationError('El usuario ingresado no existe'))
        return cleaned

    def get_user(self):
        username = self.cleaned_data['username']
        return User.objects.get(username = username)

class ChangePassword(forms.Form):
    password1 = forms.CharField(
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder':'Ingrese un password',
                'class': 'form-control',
                'autocomplete': 'off',
            }
        )
    )

    password2 = forms.CharField(
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder':'Repita  el password',
                'class': 'form-control',
                'autocomplete': 'off',
            }
        )
    )

    def clean(self):
        cleaned = super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            self.add_error('password1', forms.ValidationError('Las contraseñas no coinciden.'))


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model=User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'fecha_nacimiento',
            'lugar_nacimiento',
            'dni',
            'categoria',
            'avatar'
        )
        widgets = {
            'username': forms.TextInput(

                attrs= {
                    'class': 'form-control',
                    'required':'True'
                }
            ),
            'email': forms.TextInput(

                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),
            'nombres': forms.TextInput(

                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),
            'apellidos': forms.TextInput(

                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),

            'lugar_nacimiento': forms.Select(

                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),

        }

class ReclutarAdminForm(forms.Form):
    email = forms.CharField(
        required=True,
        widget= forms.EmailInput(
            attrs={
                'placeholder':'Ingrese un email',
                'class': 'form-control',
                'autocomplete': 'off',
                'required': 'True'
            }
        )
    )

class AdminRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña',
                'class': 'form-control'
            }
        )
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir contraseña',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model=User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'fecha_nacimiento',
            'lugar_nacimiento',
            'dni',
            'avatar'
        )
        widgets = {
            'username': forms.TextInput(

                attrs= {
                    'class': 'form-control',
                    'required':'True'
                }
            ),
            'email': forms.TextInput(

                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),
            'nombres': forms.TextInput(

                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),
            'apellidos': forms.TextInput(

                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),

            'lugar_nacimiento': forms.Select(

                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),

        }
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password1', forms.ValidationError('Las contraseñas no coinciden.'))
        if len(self.cleaned_data['password2']) < 8:
            self.add_error('password2', forms.ValidationError('La contraseña debe tener al menos 8 caracteres'))
