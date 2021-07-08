from django import  forms
from .models import Tarjeta
from django.contrib.auth import authenticate
from datetime import date

class CrearTarjetaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero'].widget.attrs['class'] = 'form-control'
        self.fields['numero'].widget.attrs['required'] = 'True'
        self.fields['numero'].widget.attrs['placeholder'] = 'Ingresa el número de la tarjeta'
        self.fields['saldo'].widget.attrs['placeholder'] = 'Ingresa el saldo que deseas agregar'
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
                    'type':'date',
                }
            ),
            'cvv': forms.TextInput(

                attrs={
                    'class':'form-control',
                    'placeholder':'Ingresa el código cvv',
                    'required': 'True'
                }
            ),

        }

    def clean_numero(self):
        numero = self.cleaned_data['numero']

        if len(numero) != 16:
            self.add_error('numero', forms.ValidationError('La tarjeta debe contener 16 digitos.'))
        elif not all(x.isdigit() for x in numero):
            self.add_error('numero', forms.ValidationError('La tarjeta solo debe contener números.'))

        return numero

    """
    def clean_fecha_vencimiento(self):
        fecha_vencimiento = self.cleaned_data['fecha_vencimiento']

        years = fecha_vencimiento.year - date.today().year

        if years == 0:

            months = date.today().month - fecha_vencimiento.month

            if months >= 0:
                self.add_error('fecha_vencimiento', forms.ValidationError('La tarjeta tiene una fecha menor o está a punto de vencerse. Por favor, intenta nuevamente.'))
        else:
            self.add_error('fecha_vencimiento', forms.ValidationError('La tarjeta tiene una fecha menor o está a punto de vencerse. Por favor, intenta nuevamente.'))

        return fecha_vencimiento
        """
    def clean_cvv(self):
        cleaned_data = super(CrearTarjetaForm, self).clean()
        cvv = str(self.cleaned_data['cvv'])
        if int(cvv.__len__()) != 3:
            self.add_error('cvv', forms.ValidationError('El cvv debe tener 3 digitos.'))
        return self.cleaned_data

    def clean_saldo(self):
        saldo = self.cleaned_data['saldo']

        if saldo < 1000:
            self.add_error('saldo', forms.ValidationError('El saldo debe ser mayor o igual a $1000'))

        return saldo

class ActualizarTarjetaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['saldo'].widget.attrs['class'] = 'form-control'
        self.fields['saldo'].widget.attrs['required'] = 'True'

    class Meta:
        model = Tarjeta
        fields = ('saldo',)

    def clean_saldo(self):
        saldo = self.cleaned_data['saldo']

        if saldo < 1000:
            self.add_error('saldo', forms.ValidationError('El saldo debe ser mayor o igual a 1000'))

        return saldo


