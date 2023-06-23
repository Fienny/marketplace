from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from main.models import Product

from .models import Cart


@login_required
def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    products = Product.objects.filter(cart=cart)

    return render(request, "cart.html", {
        'cart': cart,
        'products': products,
    })


@login_required
def add_to_cart(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    cart, created = Cart.objects.get_or_create(user=request.user)

    product.cart = cart

    cart.save()
    product.save()

    return redirect('cart')


@login_required
def remove_from_cart(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if product.cart:
        product.cart = None
        product.save()

    return redirect('cart')
