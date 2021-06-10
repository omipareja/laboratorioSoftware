from django import  forms
from .models import Libro,Category
class Createlibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('__all__')
        widgets = {
            'isbn': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'required': 'True',
                    'placeholder': 'ISBN'
                }
            ),
            'autor': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'required': 'True',
                    'placeholder':'Autor'
                }
            ),
            'categoria': forms.SelectMultiple(
                attrs= {
                    'class':'form-control'
                }
            ),
            'editorial': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'required': 'True',
                    'placeholder': 'editorial'
                }
            ),
            'idioma': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'True',
                    'placeholder': 'idioma'
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'True',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'True',
                }
            ),

        }

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')
        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'required': 'True',
                    'placeholder': 'Categoria'
                }
            )
        }