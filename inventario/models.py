from django.db import models


class Inventario(models.Model):
    nombre_producto = models.CharField(max_length=100, null=False, blank=False)
    cantidad_bodega = models.IntegerField(null=False, blank=False)
    cantidad_utilizada = models.DecimalField(decimal_places=2, max_digits=6, null=False, blank=False)
    costo_unitario = models.DecimalField(decimal_places=2, max_digits=10, null=False, blank=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    ultima_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre_producto

    @property
    def costo_mp_utilizada(self):
        return self.cantidad_utilizada * self.costo_unitario
