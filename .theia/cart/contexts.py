from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Everything added to the cart will be available on all sites.

    This will store cart content but when logged out this context will be lost
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}