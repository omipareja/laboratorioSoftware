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
                    'placeholder':'Ingresa un título',
                    'class':'form-control',
                    'requires':True
                }
            ),
            'genero':forms.TextInput(
                attrs = {
                    'placeholder': 'Ingresa un género',
                    'class': 'form-control',
                    'requires': True
                }
            ),
            'idioma': forms.TextInput(
                attrs={
                    'placeholder': 'Ingresa un idioma',
                    'class': 'form-control',
                    'requires': True
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'placeholder': 'Ingresa el contenido de la noticia',
                    'class': 'form-control',
                    'requires': True
                }
            ),

        }