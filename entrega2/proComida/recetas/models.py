from django.db import models


# Create your models here.
class Recetas(models.Model):
    title = models.TextField(max_length=200, verbose_name="Titulo")
    subtitle = models.TextField(max_length=200, verbose_name="Subtitulo")
    content = models.CharField(verbose_name="contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="recetas")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")

    class Meta:
        verbose_name = "receta"
        verbose_name_plural = "recetas"
        ordering = ['created']

    def __str__(self):
        return self.title