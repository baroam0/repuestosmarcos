

from django.core.paginator import Paginator
from django.db.models import F
from django.db.models import Q
from django.shortcuts import render
from mercaderias.models import Mercaderia


def stockminimos(request):
    resultados = Mercaderia.objects.filter(cantidad__lte=F('minimo')).order_by('descripcion')
    paginador = Paginator(resultados, 10)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1

    resultados = paginador.get_page(page)

    return render(
        request,
        "stocks/minimos.html",
        {
            "resultados": resultados
        }
    )


def stockminimospersonalizado(request):
    #resultados = Mercaderia.objects.filter(cantidad__lte=F('minimo')).order_by('descripcion')

    if "txtBuscar" in request.GET:
        parametro = request.GET.get("txtBuscar")
        resultados = Mercaderia.objects.filter(
            Q(codigo__icontains=parametro) |
            Q(descripcion__icontains=parametro)
        ).filter(cantidad__lte=F('minimo')).order_by("descripcion")
    else:
        parametro = ""
        resultados = Mercaderia.objects.none()

    paginador = Paginator(resultados, 10)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1

    resultados = paginador.get_page(page)

    return render(
        request,
        "stocks/minimos_personalizado.html",
        {
            "resultados": resultados,
            "parametro": parametro
        }
    )

# Create your views here.
