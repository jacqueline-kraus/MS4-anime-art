from django.shortcuts import render, redirect, HttpResponse

def view_cart(request):
    return render(request ,'cart/cart.html')


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
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """ Delete product from cart"""
    try:
        cart = request.session.get('cart', {})
        if item_id in cart:
            cart.pop(item_id)
            #messages.success(request, f'Removed {product.name} from your bag')
        request.session['cart'] = cart
        return redirect('view_cart')

    except Exception as e:
        #messages.error(request, f'Error removing item: {e}')
        return redirect('view_cart')
    
