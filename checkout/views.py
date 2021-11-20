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
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jo5kuAmaXqFLDCWwC3raun0GhA3Ab1wfoHzV0VH1uIZX0gro8TAM8VJbSI74wc8fObYEP7StLqoSiKX9vNsIK0400IXTWvEyY',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)