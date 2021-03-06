from django.contrib import messages
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)

from products.models import Product


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add quantity """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    messages.success(request, "Item added to cart")

    return redirect('view_cart')


def update_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Delete product from cart"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        if item_id in cart:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')
        request.session['cart'] = cart
        return redirect('view_cart')

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return redirect('view_cart')
