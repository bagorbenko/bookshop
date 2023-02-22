import pytest
from rest_framework.test import APIClient

from books.models import Category, Genre, Author, Publisher, Book, BookInstance
from cart.models import Cart, CartItem
from order.models import Order
from user.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_data():
    return {
        "username": "testuser",
        "password": "testpassword",
        "password2": "testpassword",
        "email": "testuser@example.com",
        "first_name": "Don",
        "last_name": "Joe",
    }


@pytest.fixture
def book_data():
    return {
        "title": "Test Book 1",
        "category": 1,
        "genres": [1],
        "author": [1],
        "isbn": "1234567890123",
        "pages_count": 250,
        "state": "N",
        "bind": "S",
    }


@pytest.fixture
def cart_data():
    return {
        "user": User.objects.create(username="testuser", email="test@example.com"),
        "total_price": 100.00,
    }


@pytest.fixture
def cart_item_data(cart_data, book_instance_data):
    return {
        "book_instance": book_instance_data,
        "cart": cart_data,
        "count": 2,
        "price": book_instance_data.price * 2,
    }


@pytest.fixture
def cart(cart_data):
    return Cart.objects.create(**cart_data)


@pytest.fixture
def cart_item(cart_item_data):
    return CartItem.objects.create(**cart_item_data)


@pytest.fixture
def order_data(cart_data):
    return {
        "user": cart_data["user"],
        "cart": cart_data,
        "total_price": cart_data["total_price"],
    }


@pytest.fixture
def order(order_data):
    return Order.objects.create(**order_data)


@pytest.fixture
def create_objects():
    category = Category.objects.create(name="category1", description="description1")
    genre = Genre.objects.create(name="genre1", description="description1")
    author = Author.objects.create(name="author1", biography="biography1")
    publisher = Publisher.objects.create(name="publisher1", description="description1")
    book = Book.objects.create(
        title="book1", category=category, isbn="1234567890123", pages_count=100
    )
    book.genres.add(genre)
    book.author.add(author)
    book_instance = BookInstance.objects.create(
        book=book, publisher=publisher, price=10, count=5
    )
