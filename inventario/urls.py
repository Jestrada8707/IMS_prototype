from django.urls import path
from .views import lista_inventario, producto_unitario

urlpatterns = [
    path("", lista_inventario, name="lista_inventario"),
    path("detalle_prod/<int:pk>", producto_unitario, name="producto_unitario"),
    ]
