from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
import json
from .models import Product
from .forms import ProductForm
from .cart_utils import get_or_create_cart, save_cart

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

def add_to_cart(request, product_id):
    cart = get_or_create_cart(request)
    
    if(product_id not in cart):
        cart.append(product_id)
    
    save_cart(request, cart)

    return HttpResponse(json.dumps(cart), content_type='application/json')

def cart_detail(request):
    cart = get_or_create_cart(request)
    items = Product.objects.filter(ProductId__in=cart)
    return render(request, 'productos/cart_detail.html', {'items': items})