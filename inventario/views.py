from django.shortcuts import render, get_object_or_404
from .models import Inventario
from django.contrib.auth.decorators import login_required

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
