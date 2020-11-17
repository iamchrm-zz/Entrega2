from django.shortcuts import render
from typing import OrderedDict
from django.db.models.fields import NullBooleanField
from django.db.models.manager import EmptyManager
from .models import Producto
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def productos(request):
    
    productos = Producto.objects.all()
    paginator = Paginator(productos, 4)
    productos = request.GET.get('productos')


    try:
        productos = paginator.page(productos)
    except PageNotAnInteger:
        productos = paginator.page(1)
    except EmptyPage:
        productos = paginator.page(paginator.num_page)

    return render(request,'productos/productos.html',{'productos':productos})