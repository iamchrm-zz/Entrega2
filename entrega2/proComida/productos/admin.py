from django.contrib import admin
from .models import Producto, ProductoP

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
class ProductoPAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')    

admin.site.register(Producto, ProductoAdmin)
admin.site.register(ProductoP, ProductoPAdmin)