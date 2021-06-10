from django import  forms
from .models import Libro
from applications.tarjetas.models import *
class PruebaForm(forms.Form):
    prueba = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Usuario',
                'class': 'form-control',
                'autocomplete': 'off',
                'name':'prueba'
            }
        )
    )
class MetodoPago(forms.Form):
    metodo = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'metodo de pago',
                'class': 'form-control',
                'autocomplete': 'off',
            }
        )
    )

class DevolucionForm(forms.Form):
    descripcion  = forms.CharField(
        required=True,
        widget= forms.Textarea(
            attrs={
                'class':'form-control'
            }
        )
    )