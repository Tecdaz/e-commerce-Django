# ecommerce/cart_utils.py

def get_or_create_cart(request):
    cart = request.session.get('cart', [])
    return cart

def save_cart(request, cart):
    request.session['cart'] = cart
    request.session.modified = True