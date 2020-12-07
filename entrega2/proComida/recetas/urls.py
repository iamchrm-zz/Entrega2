from django.urls import path
from . import views

urlpatterns = [
    path('recetas/', views.recetas, name='recetas'),
]