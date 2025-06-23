
import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import Venta, DetalleVenta
from .forms import DetalleVentaForm
from mercaderias.models import Unidad, Mercaderia


def descuentastock(mercaderiaid, cantidad):
    mercaderia = Mercaderia.objects.get(pk=mercaderiaid)
    cantidadexistente = mercaderia.cantidad
    cantidadactual = float(cantidadexistente) - float(cantidad)
    mercaderia.cantidad = cantidadactual
    mercaderia.save()
    

def revertirfecha(fecha):
    fecha_formato = '%d/%m/%Y'
    fecha_obj = datetime.datetime.strptime(fecha, fecha_formato)
    return fecha_obj

def rrevertirfecha(fecha):
    fecha_formato = '%Y-%m-%d'
    fecha_obj = datetime.datetime.strptime(fecha, fecha_formato)
    return fecha_obj


def controlarcantidad(mercaderia, cantidad):
    consulta = Mercaderia.objects.get(pk=mercaderia)
    cantidadmercaderia = consulta.cantidad
    operacion = float(cantidadmercaderia) - float(cantidad)
    if operacion <= 0:
        return 1
    else:
        return 0


def listadoventas(request):
    #resultados = None
    if "txtBuscar" in request.GET:
        parametro = request.GET.get("txtBuscar")
        if "/" in parametro in parametro:
            arrayparametro = parametro.split("/")
            anio = arrayparametro[2]
            mes = arrayparametro[1]
            dia = arrayparametro[0]
            resultados = Venta.objects.filter(
                fecha__year=anio, fecha__month=mes, fecha__day=dia).order_by("-pk")
        else:
            resultados = Venta.objects.all().order_by("-pk")
    else:
        resultados = Venta.objects.all().order_by("-pk")

    paginador = Paginator(resultados, 2)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1

    resultados = paginador.get_page(page)

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


def editarventa(request, pk):
    consulta = Venta.objects.get(pk=pk)
    if request.POST:
        form = DetalleVentaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA ACTUALIZADO LOS DATOS DE LA MERCADERIA")
            return redirect('/listadoventas')
        else:
            return render(request, 'ventas/venta_edit.html', {"form": form})
    else:
        form = DetalleVentaForm(instance=consulta)
        return render(request,
            'ventas/venta_edit.html',
            {"form": form}
        )


def verdetalleventa(request, pk):
    consultaventa = Venta.objects.get(pk=pk)
    resultados = DetalleVenta.objects.filter(venta=consultaventa)

    for i in resultados:
        print(i)
    
    return render(request,
        'ventas/ventas_detalle.html',
        {
            "resultados": resultados,
            "venta": consultaventa
        }
    )


@csrf_exempt
def ajaxgrabarventa(request):
    fecha = request.POST["fecha"]
    fecha = revertirfecha(fecha)

    cliente = request.POST["cliente"]

    if "pagado" in request.POST:
        pagado = True
    else:
        pagado = False

    arraymaterial = request.POST.getlist('arraymaterial[]')
    # arrayunidad = request.POST.getlist('arrayunidad[]')
    arraycantidad = request.POST.getlist('arraycantidad[]')

    venta=Venta(
        fecha=fecha,
        cliente=cliente,
        pagado=pagado
    )

    venta.save()
    orden = Venta.objects.latest("pk")

    for (material, cantidad) in zip(arraymaterial, arraycantidad):
        mercaderia = Mercaderia.objects.get(pk=int(material))
        # unidad = Unidad.objects.get(pk=int(unidad))

        operacion = controlarcantidad(mercaderia.pk, cantidad)

        if operacion == -10:
            data = {
                "status": 400
            }
            return JsonResponse(data)
        else:
            detalleventa = DetalleVenta(
                venta=venta,
                mercaderia=mercaderia,
                cantidad=cantidad,
            )

            # agregamaterial(material.pk, cantidad)
            descuentastock(mercaderia.id, cantidad)
            detalleventa.save()

            data = {
                "status": 200
            }

    return JsonResponse(data)


def borrarventa(request, pk):
    venta = get_object_or_404(Venta, pk=pk)

    if request.method == 'POST':
        venta.delete()
        return redirect('/listadoventas')
    
    return render(request, 'ventas/venta_erase.html', {'venta': venta})

# Create your views here.
