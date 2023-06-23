from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Seller


@receiver(post_save, sender=Seller)
def become_seller(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        authors_group = Group.objects.get(name='Sellers')
        authors_group.user_set.add(user)
