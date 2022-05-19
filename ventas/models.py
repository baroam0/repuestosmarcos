
from django.db import models
from mercaderias.models import Mercaderia, Unidad

class Venta(models.Model):
    fecha = models.DateField(null=False, blank=False)
    
    def __str__(self):
        return str(self.fecha)
    
    class Meta:
        verbose_name_plural = "Ventas"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    mercaderia = models.ForeignKey(Mercaderia, on_delete=models.CASCADE)
    # unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    cantidad = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False)

    def __str__(self):
        return str(self.venta)

    class Meta:
        verbose_name_plural = "Detalles de Ventas"

# Create your models here.
