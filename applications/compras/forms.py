from django import  forms
from .models import Libro
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