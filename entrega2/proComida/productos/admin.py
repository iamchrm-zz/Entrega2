from django.contrib import admin
from .models import Producto, postP	

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
class postPAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(postP, postPAdmin)
admin.site.register(Producto, ProductoAdmin)