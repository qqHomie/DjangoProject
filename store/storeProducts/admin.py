from django.contrib import admin
from .models import ProductCategory, Product, Basket

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Basket)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category',)
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)