
from django.shortcuts import render
from .models import Venta


def listadoventas(request):
    resultados = None
    if "txtBuscar" in request.GET:
        parametro = request.GET.get("txtBuscar")
        resultados = Venta.objects.filter(fecha__icontains=parametro)

    return render(
        request,
        "mercaderias/listadomercaderias.html",
        {
            "resultados": resultados
        }
    )


def nuevaventa(request):
    if request.POST:
        form = MercaderiaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA GRABADO EL MATERIAL")
            return redirect('/listadomercaderias')
        else:
            return render(request, 'mercaderias/mercaderia_edit.html', {"form": form})
    else:
        form = MercaderiaForm()
        return render(request, 'mercaderias/mercaderia_edit.html', {"form": form})


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
