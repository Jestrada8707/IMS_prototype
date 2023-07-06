from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventario
from django.contrib.auth.decorators import login_required
from .forms import AgregarInventarioform, ActualizarInventarioform


@login_required
def lista_inventario(request):
    inventarios = Inventario.objects.all()
    context = {
        "title": "Listado Inventario",
        "inventarios": inventarios
    }
    return render(request, template_name="inventario/listado_inventario.html", context=context)


@login_required
def producto_unitario(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    context = {
        "inventario": inventario
    }

    return render(request, "inventario/producto_detallado.html", context=context)


@login_required()
def agregar_producto(request):
    if request.method == "POST":
        add_form = AgregarInventarioform(data=request.POST)
        nuevo_inventario = add_form.save(commit=False)
        nuevo_inventario.sales = float(add_form.data['costo_unitario']) * float(add_form.data['cantidad_bodega'])
        nuevo_inventario.save()
        return redirect("/inventario/")
    else:
        add_form = AgregarInventarioform()

    return render(request, "inventario/agregar_inventario.html", {'form': add_form})


@login_required
def borrar_inventario(request, pk):
    producto = get_object_or_404(Inventario, pk=pk)
    producto.delete()
    return redirect("/inventario/")


@login_required()
def actualizar_producto(request, pk):
    producto = get_object_or_404(Inventario, pk=pk)
    if request.method == "POST":
        update_form = AgregarInventarioform(data=request.POST)
        if update_form.is_valid():
            producto.nombre_producto = update_form.data['nombre_producto']
            producto.cantidad_bodega = update_form.data['cantidad_bodega']
            producto.cantidad_utilizada = update_form.data['cantidad_utilizada']
            producto.costo_unitario = update_form.data['costo_unitario']
            producto.sales = float(producto.costo_unitario) * float(producto.cantidad_bodega)
            producto.save()
            return redirect(f"/inventario/detalle_prod/{pk}")

    else:
        update_form = AgregarInventarioform(instance=producto)

    context = {"form": update_form}
    return render(request, "inventario/actualizar_producto.html", context=context)
