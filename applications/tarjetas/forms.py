from django import  forms
from .models import Tarjeta
from django.contrib.auth import authenticate

class CrearTarjetaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero'].widget.attrs['class'] = 'form-control'
        self.fields['numero'].widget.attrs['required'] = 'True'
        self.fields['numero'].widget.attrs['placeholder'] = 'Numero de la tarjeta'
        self.fields['saldo'].widget.attrs['placeholder'] = 'saldo'
        self.fields['saldo'].widget.attrs['required'] = 'True'



    class Meta:

        model=Tarjeta
        fields = (
            'numero',
            'fecha_vencimiento',
            'cvv',
            'saldo'
        )
        widgets = {

            'fecha_vencimiento': forms.DateInput(

                attrs={
                    'type':'date'
                }
            ),
            'cvv': forms.TextInput(

                attrs={
                    'class':'form-control',
                    'placeholder':'codigo cvv',
                    'required': 'True'
                }
            ),

        }
    def clean_cvv(self):
        cleaned_data = super(CrearTarjetaForm, self).clean()
        cvv = str(self.cleaned_data['cvv'])
        if int(cvv.__len__()) != 3:
            self.add_error('cvv', forms.ValidationError('El cvv debe tener 3 digitos'))
        return self.cleaned_data

class ActualizarTarjetaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['saldo'].widget.attrs['class'] = 'form-control'
        self.fields['saldo'].widget.attrs['required'] = 'True'

    class Meta:
        model = Tarjeta
        fields = ('saldo',)



