
from django import forms
from django.db.models import fields

from .models import Mercaderia, Unidad


class MercaderiaForm(forms.ModelForm):

    descripcion = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "pure-input-1", 'placeholder':'Descripcion'})
        )

    unidad = forms.ModelChoiceField(
        required=True,
        queryset=Unidad.objects.all(),
        widget=forms.ModelChoiceField(attrs={'class':'pure-input-1'}))

    cantidad = forms.IntegerField(required=True)

    class Meta:
        model = Mercaderia
        fields = ["descripcion", "unidad", "cantidad"]
