from django.urls import path

from .views import add_to_cart, remove_from_cart, cart

urlpatterns = [
    path('add_object/<product_pk>', add_to_cart, name='add_to_cart'),
    path('remove_object/<product_pk>', remove_from_cart, name='remove_from_cart'),
    path('', cart, name='cart')
]