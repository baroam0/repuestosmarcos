
from django.db.models import F
from django.shortcuts import render
from mercaderias.models import Mercaderia


def stockminimos(request):
    
    resultados = Mercaderia.objects.filter(cantidad__lte=F('minimo'))

    return render(
        request,
        "stocks/minimos.html",
        {
            "resultados": resultados
        }
    )

# Create your views here.
