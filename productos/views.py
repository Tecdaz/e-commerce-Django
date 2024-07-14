from django.shortcuts import render
from django.views import generic
import json
from .models import Product
from .forms import ProductForm

# Create your views here.

def vista_inicio(request):
    productos = Product.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'productos/inicio.html', context)

def vista_productos_category(request, *args, **kwargs):
    request_category = kwargs.get('category')
    productos = Product.objects.filter(Category=request_category)
    context = {
        'productos': productos
    }
    return render(request, 'productos/_productos.html', context)

def vista_producto(request, *args, **kwargs):
    request_id = kwargs.get('id')
    producto = Product.objects.get(ProductId=request_id)
    print(producto)
    context = {
        'producto': producto
    }
    return render(request, 'productos/producto.html', context)


def vista_categorias(request):
    categorias = Product.objects.values('Category').distinct()
    print(categorias)
    context = {
        'categorias': categorias
    }
    return render(request, 'productos/categorias.html', context)

def vista_contacto(request):
    return render(request, 'productos/contacto.html')