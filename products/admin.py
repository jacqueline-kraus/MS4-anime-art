from django.contrib import admin
from .models import Product, Type

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'type',
        'price',
        'image',
    )

    ordering = ('sku',)

class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Type, TypeAdmin)
