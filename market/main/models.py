from django.db import models
from django.contrib.auth.models import User

from cart.models import Cart


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False)
    num_of_goods = models.IntegerField(blank=False)

    class Meta:
        permissions = (("add_product", "can add product"),
                       ("change_product", "can change product"),
                       ("delete_product", "can delete product"))

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128, blank=False)
    description = models.TextField(blank=False)
    images = models.ImageField(upload_to="gallery")
    tags = models.CharField(max_length=128)
    quantity = models.IntegerField(blank=False)
    price = models.FloatField(default=0.0)
    seller = models.ForeignKey(to="Seller", on_delete=models.CASCADE)
    category = models.ManyToManyField(to="Category")
    cart = models.ForeignKey("cart.Cart", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return self.name
