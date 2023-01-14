from django.db import models
from cart.models import Cart


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0)

    @staticmethod
    def place_order(user):
        cart = Cart.objects.get(user=user)
        order = Order.objects.create(user=user)
        order.books.set(cart.books.all())
        cart.books.clear()
        return order

    def update_total_price(self):
        total_price = 0
        for book in self.books.all():
            total_price += book.price
        self.total_price = total_price
        self.save()
    # def save(self, *args, **kwargs):
    #     for item in self.cart.books.select_related('cart_items').all():
    #         book_instance = item.item
    #         book_instance.count -= item.count_item
    #         book_instance.save()
    #         self.total_price += book_instance.price*item.count_item
    #     return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
