
from django import forms
from django.forms import fields

from mercaderias.models import Mercaderia, Unidad


class MercaderiaForm(forms.ModelForm):
    codigo = forms.CharField(
        required=True, widget=forms.TextInput({'class':'pure-input-1', 'placeholder':'Codigo'}))

    descripcion = forms.CharField(
        required=True, widget=forms.TextInput({'class':'pure-input-1', 'placeholder':'Descripcion'}))

    cantidad = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            {
                'class':'pure-input-1',
                'placeholder':'Stock'
            }
        )
    )

    pieza = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(
            {
                'class':'pure-input-1',
                'placeholder':'Pieza'
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
        fields = ['codigo', 'descripcion', 'cantidad', 'pieza', 'minimo'] 
