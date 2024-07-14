from django import forms
from django.contrib import admin

from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['ProductId', 'ProductTitle', 'Category']
    search_fields = ['ProductTitle', 'Category']

admin.site.register(Product, ProductAdmin)