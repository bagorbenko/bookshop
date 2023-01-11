from django.db import models
from user.models import Account
from books.models import BookInstances


class Cart(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    books = models.ManyToManyField(BookInstances, through="CartBook")

    @property
    def count(self):
        return self.user.name()

    @property
    def price(self):
        result = 0
        for i in self.books.prefetch_related('books').all():
            result += i.books.price * i.count_books
        return result

    def __str__(self):
        return f'{self.user.first_name} Cart'


class CartBook(models.Model):
    book_instance = models.ForeignKey(BookInstances, on_delete=models.CASCADE, related_name="book_instance")
    count_books = models.PositiveIntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")

