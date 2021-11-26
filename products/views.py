from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Type
from .forms import ProductForm


def products(request):

    products = Product.objects.all()
    query = None
    types = None

    if request.GET:
        if 'type' in request.GET:
            types = request.GET['type'].split(',')
            products = products.filter(type__name__in=types)
            types = Type.objects.filter(name__in=types)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter your search criteria")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products, 
        'search_term': query,
        'current_types': types,
    }

    return render(request ,'products/products.html', context)


def product_display(request, product_id):
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product, 
    }

    return render(request,'products/product_display.html', context)


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added product successfully.')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Product could not be added. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product successfully updated.')
            return redirect(reverse('product_display', args=[product.id]))
        else:
            messages.error(request, 'Product could not be updated. Please check the form.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are updating {product.name}')
    
    template = 'products/update_product.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted.')
    return redirect(reverse('products'))

