from django.db import models

from cart.models import Cart
from user.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='order')
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Заказ {self.pk} для пользователя {self.user.first_name}'

    def calculate_total_price(self):
        items = self.cart.cart_items.all()
        total_price = 0
        for item in items:
            total_price += item.count * item.book_instance.price
        return total_price

    def save(self, *args, **kwargs):
        for item in self.cart.cart_items.all():
            if item.book_instance.count < item.count:
                raise ValueError("Не хватает книг в магазине")
        self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)
        for item in self.cart.cart_items.all():
            item.book_instance.count -= item.count
            item.book_instance.save()
            item.delete()


    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"



