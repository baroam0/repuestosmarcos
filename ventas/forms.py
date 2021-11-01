
from django import forms
from django.db.models import query
from .models import DetalleVenta
from mercaderias.models import Unidad, Mercaderia

class DetalleVentaForm(forms.ModelForm):
    mercaderia = forms.ModelChoiceField(Mercaderia, required=True)
    unidad = forms.ModelChoiceField(queryset=Unidad.objects.all(), required=True)
    cantidad = forms.DecimalField(required=True)


