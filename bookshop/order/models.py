import json

import requests
from django.db import models, transaction

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

    def send_purchase_data(self):
        data = []
        for item in self.cart.cart_items.all():
            item_data = {
                "order_id": self.id,
                "book_id": item.book_instance.book.id,
                "user_id": self.user.id,
                "book_title": item.book_instance.book.title,
                "author_name": item.book_instance.book.author.name,
                "price": item.price,
                "create_at": self.created_at,
                "publisher_id": item.book_instance.book.publisher.id,
            }
            data.append(item_data)
        print("\n\n", data)
        requests.post("http://127.0.0.1:5050/purchases/", json=data)

    @transaction.atomic
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
        self.cart.cart_items.all().delete()
        self.cart.update_total_price()
        self.send_purchase_data()
        self.cart.save()

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"



