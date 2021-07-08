from django import  forms
from .models import Libro,Category
import re
class Createlibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('__all__')
        widgets = {
            'isbn': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'required': 'True',
                    'placeholder': 'Ingresa el ISBN sin guiones'
                }
            ),
            'titulo': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'required': 'True',
                    'placeholder': 'Ingresa el titulo del libro'
                }
            ),
            'autor': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'required': 'True',
                    'placeholder':'Ingresa el nombre de los autores'
                }
            ),
            'categoria': forms.SelectMultiple(
                attrs= {
                    'class':'form-control',
                    'required': 'True',
                }
            ),
            'editorial': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'required': 'True',
                    'placeholder': 'Ingresa la editorial'
                }
            ),
            'idioma': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'True',
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'True',
                }
            ),
        }

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        regex = '^[0-9]'

        if not re.match(regex, isbn):
            self.add_error('isbn', forms.ValidationError('El ISBN solo debe contener números.'))

        return isbn

    def clean_numero_paginas(self):
        numero_paginas = self.cleaned_data['numero_paginas']

        if numero_paginas < 1:
            self.add_error('numero_paginas', forms.ValidationError('El número de páginas debe ser mayor o igual a 1'))

        return numero_paginas

    def clean_precio(self):
        precio = self.cleaned_data['precio']

        if precio < 1:
            self.add_error('precio', forms.ValidationError('El precio debe ser mayor o igual a 1'))

        return precio

    def clean_stock(self):
        stock = self.cleaned_data['stock']

        if stock < 1:
            self.add_error('stock', forms.ValidationError('El stock debe ser mayor o igual a 1'))

        return stock

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')
        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'required': 'True',
                    'placeholder': 'Ingresa el nombre de la categoria'
                }
            )
        }