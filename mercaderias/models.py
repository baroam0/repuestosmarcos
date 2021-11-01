
from django.db import models


class Unidad(models.Model):
    """Clase para las Unidades """    
    descripcion = models.CharField(
        max_length=255,blank=False, null=False, unique=True)

    def __str__(self):
        """Retorno del nombre de la Unidad"""
        return self.descripcion

    class Meta:
        """Meta de la Unidad """
        verbose_name_plural = "Unidades"


class Mercaderia(models.Model):
    """Clase para las Mercaderias """
    descripcion = models.CharField(
        max_length=255,blank=False, null=False, unique=True)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2,null=False, blank=False)

    def __str__(self):
        """Retorno del nombre de la Mercaderia"""
        return self.descripcion

    class Meta:
        """Meta de la Mercaderia """
        verbose_name_plural = "Mercaderias"


# Create your models here.
