
from django.db import models
from mercaderias.models import Mercaderia, Unidad

class Venta(models.Model):
    fecha = models.DateField(null=False, blank=False)
    
    def __str__(self):
        return self.fecha
    
    class Meta:
        verbose_name_plural = "Ventas"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    mercaderia = models.ForeignKey(Mercaderia, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    cantidad = models.DecimalField(blank=False, null=False)

    def __str__(self):
        return self.venta

    class Meta:
        verbose_name_plural = "Detalles de Ventas"

# Create your models here.