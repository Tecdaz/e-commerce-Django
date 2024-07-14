from django.urls import path

from . import views

urlpatterns = [
    path("productos/<str:category>", views.vista_productos_category, name="vista_productos_category"),
    path("producto/<int:id>", views.vista_producto, name="vista_producto"),
    path("categorias/", views.vista_categorias, name="vista_categorias"),
    path("", views.vista_inicio, name="vista_inicio"),
    path("contacto/", views.vista_contacto, name="vista_contacto"),
    path("add_to_cart/<int:product_id>", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart_detail, name="cart_detail"),
]
