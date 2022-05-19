
from django import forms
from django.db.models import query
from django.forms import fields
from .models import DetalleVenta
from mercaderias.models import Unidad, Mercaderia


class DetalleVentaForm(forms.ModelForm):
    mercaderia = forms.ModelChoiceField(
        queryset=Mercaderia.objects.all().order_by("descripcion"),
        required=True,
        widget=forms.Select({'class':'pure-input-1'})
    )
    """
    unidad = forms.ModelChoiceField(
        queryset=Unidad.objects.all(),
        required=True,
        widget=forms.Select({'class':'pure-input-1'})
        )
    """
    cantidad = forms.DecimalField(
        required=True,
        widget=forms.NumberInput({'class':'pure-input-1'}))

    class Meta:
        model = DetalleVenta
        fields = ['mercaderia','cantidad']
        
