import factory

from order.models import Order
from tests.books.factories import BookFactory
from user.models import User
from cart.models import Cart, CartItem
from books.models import BookInstance


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class BookInstanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BookInstance

    book = factory.SubFactory(BookFactory)
    count = 1
    price = factory.Faker('random_int', min=1, max=1000)


class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cart
    user = factory.SubFactory(UserFactory)


class CartItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CartItem

    cart = factory.SubFactory(CartFactory)
    book_instance = factory.SubFactory(BookInstanceFactory)
    count = factory.Faker('random_int', min=1, max=5)


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    user = factory.SubFactory(UserFactory)