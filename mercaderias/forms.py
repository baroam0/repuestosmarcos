
from django import forms
from django.forms import fields

from mercaderias.models import Mercaderia, Unidad


class MercaderiaForm(forms.ModelForm):
    descripcion = forms.CharField(
        required=True, widget=forms.TextInput({'class':'pure-input-1', 'placeholder':'Descripcion'}))
    unidad = forms.ModelChoiceField(
        required=True,
        queryset=Unidad.objects.all(),
        widget=forms.Select({'class':'pure-input-1'})
        )
    cantidad = forms.DecimalField(
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
        fields = ['descripcion', 'unidad', 'cantidad'] 
