from django.db import models
from django.shortcuts import redirect, get_object_or_404
from user.models import User
from books.models import BookInstances


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='cart')
    books = models.ManyToManyField(BookInstances, through='CartBook')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def add_book_to_cart(request, book_id):
        book = get_object_or_404(BookInstances, pk=book_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        try:
            cart_item = CartItem.objects.get(cart=cart, book=book)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            CartItem.objects.create(cart=cart, book=book, quantity=1)
        cart.update_total()
        return redirect('cart_detail')

    def update_total(self):
        total = 0
        for item in self.cartitem_set.all():
            total += item.book.price * item.quantity
        self.total_price = total
        self.save()

    def __str__(self):
        return f'{self.user.first_name} Cart'


class CartItem(models.Model):
    book_instance = models.ForeignKey(BookInstances, on_delete=models.CASCADE, related_name="book_instance")
    count_books = models.PositiveIntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.IntegerField()
