from django import forms
from .models import Noticias

class CrearNoticiaForm(forms.ModelForm):
    class Meta:

        model = Noticias
        fields = (
            'titulo',
            'genero',
            'idioma',
            'descripcion',
            'imagen'
        )

        widgets = {
            'titulo':forms.TextInput(
                attrs = {
                    'placeholder':'titulo',
                    'class':'form-control',
                    'requires':True
                }
            ),
            'genero':forms.TextInput(
                attrs = {
                    'placeholder': 'genero',
                    'class': 'form-control',
                    'requires': True
                }
            ),
            'idioma': forms.TextInput(
                attrs={
                    'placeholder': 'idioma',
                    'class': 'form-control',
                    'requires': True
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'placeholder': 'Descripcion',
                    'class': 'form-control',
                    'requires': True
                }
            ),

        }