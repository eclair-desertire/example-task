from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import  User
from books.models import Favourites


@receiver(post_save, sender=User)
def create_favourites(sender, instance=None, created=False, **kwargs):
    if created:
        Favourites.objects.create(user=instance)