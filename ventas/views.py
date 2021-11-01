
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Venta
from .forms import DetalleVentaForm

def listadoventas(request):
    resultados = None
    if "txtBuscar" in request.GET:
        parametro = request.GET.get("txtBuscar")
        resultados = Venta.objects.filter(fecha__icontains=parametro)

    return render(
        request,
        "ventas/listadoventa.html",
        {
            "resultados": resultados
        }
    )


def nuevaventa(request):
    if request.POST:
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA GRABADO LA VENTA")
            return redirect('/listadoventas')
        else:
            return render(request, 'ventas/venta_edit.html', {"form": form})
    else:
        form = DetalleVentaForm()
        return render(request, 'ventas/venta_edit.html', {"form": form})


def editarmercaderia(request, pk):
    consulta = Mercaderia.objects.get(pk=pk)
    if request.POST:
        form = MercaderiaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA ACTUALIZADO LOS DATOS DE LA MERCADERIA")
            return redirect('/listadomercaderias')
        else:
            return render(request, 'mercaderias/mercaderia_edit.html', {"form": form})
    else:
        form = MercaderiaForm(instance=consulta)
        return render(request,
            'mercaderias/mercaderia_edit.html',
            {"form": form}
        )


# Create your views here.
