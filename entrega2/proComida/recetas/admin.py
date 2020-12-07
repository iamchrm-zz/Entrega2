from django.contrib import admin
from .models import Recetas

# Register your models here.
class RecetaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Recetas, RecetaAdmin)
# Register your models here.
