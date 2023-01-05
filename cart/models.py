from django.db import models
from user.models import Account
from books.models import BookInstance


class ItemForCart(models.Model):
    item = models.ForeignKey(BookInstance, on_delete=models.SET_NULL, null=True)
    count_item = models.IntegerField()


class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    books = models.ManyToManyField(ItemForCart)


    @property
    def count(self):
        return self.user.name()

    @property
    def price(self):
        result = 0
        for i in self.books.select_related('item').all():
            result += i.item.price * i.count_item
        return result

    def __str__(self):
        return f'{self.user.first_name} Cart'

