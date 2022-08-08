
from django import forms
from django.forms import fields

from mercaderias.models import Mercaderia, Unidad


class MercaderiaForm(forms.ModelForm):
    descripcion = forms.CharField(
        required=True, widget=forms.TextInput({'class':'pure-input-1', 'placeholder':'Descripcion'}))

    codigo = forms.CharField(
        required=True, widget=forms.TextInput({'class':'pure-input-1', 'placeholder':'Codigo'}))


    cantidad = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            {
                'class':'pure-input-1',
                'placeholder':'Cantidad'
            }
        )
    )
    minimo = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            {
                'class':'pure-input-1',
                'placeholder':'Cantidad'
            }
        )
    )

    class Meta:
        model = Mercaderia
        fields = ['descripcion', 'codigo', 'cantidad', 'minimo'] 
