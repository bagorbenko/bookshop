from django.db import models
from django.shortcuts import redirect, get_object_or_404
from user.models import User
from books.models import BookInstances
from django.db.models.signals import post_save
from django.dispatch import receiver


class CartItem(models.Model):
    book_instance = models.ForeignKey(BookInstances, on_delete=models.CASCADE, related_name="book_instance")
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.IntegerField()

    def get_total_price(self):
        return self.book.price * self.quantity

    def __str__(self):
        return f'Книги для корзины {self.cart.user.first_name} - {self.quantity}'


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='cart')
    books = models.ManyToManyField(BookInstances, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def total_items(self):
        return self.books.count()

    def update_total_price(self):
        total_price = 0
        for cart_item in self.cart_items.all():
            total_price += cart_item.get_total_price()
        self.total_price = total_price
        self.save()

    def __str__(self):
        return f'{self.user.first_name} Cart  - Itmes {self.total_items()} - {self.total_price}'

    @receiver(post_save, sender=User)
    def create_cart(sender, instance, created, **kwargs):
        if created:
            Cart.objects.create(user=instance)

