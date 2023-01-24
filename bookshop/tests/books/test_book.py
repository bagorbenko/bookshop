import json

import pytest
from rest_framework import status

from books.models import Book
from tests.books.factories import BookFactory


@pytest.mark.django_db
def test_create_book():
    book = Book.objects.create(
    title='Test Book',
    isbn='1234567890',
    pages_count=200
    )
    assert Book.objects.filter(title='Test Book').exists()
    assert book.isbn == '1234567890'
    assert book.pages_count == 200
    book.delete()
    assert not Book.objects.filter(title='Test Book').exists()


@pytest.mark.django_db
def test_get_books(api_client):
    # Создаем книгу с помощью фабрики
    book = BookFactory()
    book.save()

    # Отправляем GET-запрос к API
    url = "/api/books/"
    response = api_client.get(url)

    # Проверяем статус ответа
    assert response.status_code == status.HTTP_200_OK

    # Проверяем, что в ответе содержится одна книга
    response_data = json.loads(response.content)
    assert len(response_data) == 1
    # Проверяем данные книги
    assert response_data[0]['title'] == book.title
    # assert response_data[0]['isbn'] == book.isbn
    # assert response_data[0]['pages_count'] == book.pages_count