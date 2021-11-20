from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from stripe.api_resources import product

from cart import contexts

from .forms import CheckoutForm
from products.models import Product
from .models import Order, OrderLineItem
from cart.contexts import cart_contents

import stripe

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'street_address': request.POST['street_address'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'country': request.POST['country'],
        }
        order_form = CheckoutForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "We cannot find one of the products in your cart. Please contact us for help.")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))
            request.session['save.info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'An error ocurred. Please check your information.')
    else: 
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is empty. There is nothing to purchase.")
            return redirect(reverse('products'))
        
        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount = stripe_total,
            currency = settings.STRIPE_CURRENCY,
        )

        order_form = CheckoutForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order was successful! \
        Your order number is {order_number}. \
            A confrmation email will be sent to {order.email} soon.')
    
    if 'cart' in request.session:
        del request.session['cart']
    
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)