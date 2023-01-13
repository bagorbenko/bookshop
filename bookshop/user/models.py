from django.contrib.auth.models import AbstractUser
from cart.models import Cart
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):

    def __str__(self):
        return self.first_name


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
