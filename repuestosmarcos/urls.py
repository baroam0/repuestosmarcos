"""repuestosmarcos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import home
from mercaderias.views import listadomercaderias, nuevamercaderia, editarmercaderia, borrarmercaderia
from ventas.views import listadoventas, nuevaventa, editarventa, verdetalleventa, ajaxgrabarventa
from stocks.views import stockminimos, stockminimospersonalizado

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('listadomercaderias/', listadomercaderias),
    path('nuevamercaderia/', nuevamercaderia),
    path('editarmercaderia/<int:pk>', editarmercaderia),
    path('borrarmercaderia/<int:pk>', borrarmercaderia),
    path('listadoventas/', listadoventas),
    path('nuevaventa/', nuevaventa),
    path('ajaxgrabarventa/', ajaxgrabarventa),
    path('editarventa/<int:pk>', editarventa),
    path('verdetalleventa/<int:pk>', verdetalleventa),
    path('listadominimos/', stockminimos),
    path('listadopersonalizado/', stockminimospersonalizado),
]
