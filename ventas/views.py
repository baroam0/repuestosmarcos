
import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import Venta, DetalleVenta
from .forms import DetalleVentaForm
from mercaderias.models import Unidad, Mercaderia


def revertirfecha(fecha):
    fecha_formato = '%d/%m/%Y'
    fecha_obj = datetime.datetime.strptime(fecha, fecha_formato)
    return fecha_obj


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


@csrf_exempt
def ajaxgrabarventa(request):
    fecha = request.POST["fecha"]
    fecha = revertirfecha(fecha)

    arraymaterial = request.POST.getlist('arraymaterial[]')
    arrayunidad = request.POST.getlist('arrayunidad[]')
    arraycantidad = request.POST.getlist('arraycantidad[]')

    print(arraymaterial)
    print(arrayunidad)
    print(arraycantidad)

    venta=Venta(
        fecha=fecha,
    )

    venta.save()
    orden = Venta.objects.latest("pk")

    for (material, unidad, cantidad) in zip(arraymaterial, arrayunidad, arraycantidad):
        mercaderia = Mercaderia.objects.get(pk=int(material))
        unidad = Unidad.objects.get(pk=int(unidad))

        detalleventa = DetalleVenta(
            venta=venta,
            mercaderia=mercaderia,
            cantidad=cantidad,
            unidad=unidad
        )

        # agregamaterial(material.pk, cantidad)

        #detalleorden.save()

    data = {
        "status": 200
    }

    return JsonResponse(data)
# Create your views here.
