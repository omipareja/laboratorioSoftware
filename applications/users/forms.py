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

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Contraseña',
                'class': 'form-control'
            }
        )
    )

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña',
                'class': 'form-control'
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
