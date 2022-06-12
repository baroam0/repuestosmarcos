

from django.core.paginator import Paginator
from django.db.models import F
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

# Create your views here.
