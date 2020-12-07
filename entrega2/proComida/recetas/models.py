from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.contrib.auth.models import User


# Create your models here.
class Receta(models.Model):
    title = models.TextField(max_length=200, verbose_name="Titulo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha creación")

    class Meta:
        verbose_name = "Categorias"
        verbose_name_plural = "Categoria de Recetas"
        ordering = ['created']

    def __str__(self):
        return self.title

class post(models.Model):
    title = models.TextField(max_length=200, verbose_name="Titulo")
    subtitle = models.TextField(max_length=200, verbose_name="Subtitulo")
    image = models.ImageField(verbose_name="Imagen", upload_to="recetas")
    content = models.CharField(max_length=200, verbose_name="contenido")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=DO_NOTHING)
    categories = models.ManyToManyField(Receta, verbose_name="categorias", related_name="get_posts" )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha creación")

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ['created']

    def __str__(self):
        return self.title