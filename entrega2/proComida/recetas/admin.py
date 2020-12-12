from django.contrib import admin
from .models import Receta
# Register your models here.
class RecetaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Receta, RecetaAdmin)
