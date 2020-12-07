from django.contrib import admin
from .models import Receta, post

# Register your models here.
class RecetaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class postAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Receta, RecetaAdmin)
admin.site.register(post, postAdmin)
# Register your models here.
