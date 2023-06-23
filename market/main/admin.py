from django.contrib import admin

from .models import Product, Seller, Category

admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(Category)
