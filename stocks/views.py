
from django.shortcuts import render
from mercaderias.models import Mercaderia


def stockminimos(request):
    resultados = Mercaderia.objects.filter(cantidad__lte=10)

    return render(
        request,
        "stocks/minimos.html",
        {
            "resultados": resultados
        }
    )

# Create your views here.
