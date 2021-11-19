from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import CheckoutForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty. There is nothing to purchase.")
        return redirect(reverse('products'))
    
    order_form = CheckoutForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }

    return render(request, template, context)