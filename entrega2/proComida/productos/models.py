from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.contrib.auth.models import User
# Create your models here.

class Producto(models.Model):
    title = models.CharField(max_length=50, verbose_name="titulo")
    created = models.DateTimeField( auto_now_add=True, verbose_name="Fecha creación") 
    updated = models.DateTimeField( auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categoria de productos"
        ordering = ['created']

    def __str__(self):
        return self.title    
class postP(models.Model):
    title = models.TextField(max_length=50, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to='productos')
    link = models.URLField(verbose_name="Más información", max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=DO_NOTHING)
    categories = models.ManyToManyField(Producto, verbose_name="categorias", related_name="get_posts" )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha creación")

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ['created']

    def __str__(self):
        return self.title