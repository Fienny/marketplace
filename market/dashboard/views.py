from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from main.models import Seller, Product


@login_required
def index(request):
    products = Product.objects.filter(seller=Seller.objects.get(user=request.user))
    return render(request, 'dashboard.html', {
        'products': products
    })
