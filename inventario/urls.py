from django.urls import path
from .views import lista_inventario, producto_unitario, agregar_producto, borrar_inventario, actualizar_producto

urlpatterns = [
    path("", lista_inventario, name="lista_inventario"),
    path("detalle_prod/<int:pk>", producto_unitario, name="producto_unitario"),
    path("agregar_inventario/", agregar_producto, name="agregar_inventario"),
    path("borrar/<int:pk>", borrar_inventario, name="borrar_inventario"),
    path("actualizar_prod/<int:pk>", actualizar_producto, name="actualizar_producto"),
]
