

from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse 
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Mercaderia, Unidad
from .forms import MercaderiaForm


def listadomercaderias(request):
    resultados = None
    if "txtBuscar" in request.GET:
        parametro = request.GET.get("txtBuscar")
        resultados = Mercaderia.objects.filter(
            Q(codigo__icontains=parametro) |
            Q(descripcion__icontains=parametro)
        ).order_by("descripcion")
    else:
        parametro = None
        resultados = Mercaderia.objects.all()
    
    paginador = Paginator(resultados, 10)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1

    resultados = paginador.get_page(page)

    return render(
        request,
        "mercaderias/listadomercaderias.html",
        {
            "resultados": resultados, 
            "parametro": parametro
        }
    )


def nuevamercaderia(request):
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


def borrarmercaderia(request, pk):
    mercaderia = get_object_or_404(Mercaderia, pk=pk)

    if request.method == 'POST':
        mercaderia.delete()
        return redirect('/listadomercaderias')

    return render(request, 'mercaderias/mercaderia_erase.html', {'mercaderia': mercaderia})
    

# Create your views here.
