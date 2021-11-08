from django.shortcuts import get_object_or_404, render
from .models import Product

def product_list(request):

    products = Product.objects.all()

    context = {
        'products': products, 
    }

    return render(request ,'products/products.html', context)


def product_display(request, product_id):
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product, 
    }

    return render(request ,'products/product_display.html', context)
