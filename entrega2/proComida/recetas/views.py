from django.shortcuts import render
from .models import Recetas
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def recetas(request):
    return render(request,'recetas/recetas.html')

def recetas(request):
    
    recetas = Recetas.objects.all()
    paginator = Paginator(recetas, 4)
    recetas = request.GET.get('recetas')


    try:
        recetas = paginator.page(recetas)
    except PageNotAnInteger:
        recetas = paginator.page(1)
    except EmptyPage:
        recetas = paginator.page(paginator.num_page)

    return render(request,'recetas/recetas.html',{'recetas':recetas})