from django.db import models
from user.models import User
from books.models import BookInstances
from django.db.models.signals import post_save
from django.dispatch import receiver


class CartItem(models.Model):
    book_instance = models.ForeignKey(BookInstances, on_delete=models.CASCADE, related_name="book_instance")
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name="items")
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0, editable=False)

    def get_total_price(self):
        self.price = self.book_instance.price * self.quantity
        return self.price

    def __str__(self):
        return f'{self.quantity} шт. книги {self.book_instance.book.title} {self.get_total_price()}'


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default=0, editable=False)

    def total_items(self):
        return self.items.count()

    def update_total_price(self):
        total_price = 0
        for item in self.items.all():
            total_price += item.get_total_price()
            print(total_price)
        self.total_price = total_price
        self.save()

    def __str__(self):
        return f'Корзина пользователя {self.user.username} {self.update_total_price()}'

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    @receiver(post_save, sender=User)
    def create_cart(sender, instance, created, **kwargs):
        if created:
            Cart.objects.create(user=instance)

