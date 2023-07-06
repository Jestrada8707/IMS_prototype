from django.forms import ModelForm
from .models import Inventario


class AgregarInventarioform(ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre_producto', 'cantidad_bodega', 'cantidad_utilizada', 'costo_unitario']

class ActualizarInventarioform(ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre_producto', 'cantidad_bodega', 'cantidad_utilizada', 'costo_unitario']