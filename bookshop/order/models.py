from django.db import models
from cart.models import Cart
from user.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name='order')
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for item in self.cart.items.all():
            item.book_instance.count -= item.quantity
            item.book_instance.save()

    def __str__(self):
        return f'Заказ {self.pk} для пользователя {self.user.first_name}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
