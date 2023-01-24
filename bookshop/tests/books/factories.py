from factory.django import DjangoModelFactory
from books.models import Book


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = "Test Book"
    isbn = 123423211
    pages_count = 123
