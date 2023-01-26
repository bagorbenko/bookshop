import json
import pytest
from rest_framework import status

from books.models import Book
from tests.books.factories import BookFactory, AuthorsFactory


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
    book = BookFactory()
    book.save()
    url = "/api/books/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    response_data = json.loads(response.content)
    assert len(response_data) == 1
    assert response_data[0]['title'] == book.title


@pytest.mark.django_db
def test_category_list(api_client, create_objects):
    response = api_client.get('/api/categories/')
    assert response.status_code == 200
    assert response.data[0]['name'] == 'category1'
    assert response.data[0]['description'] == 'description1'


@pytest.mark.django_db
def test_genre_list(api_client, create_objects):
    response = api_client.get('/api/genres/')
    assert response.status_code == 200
    assert response.data[0]['name'] == 'genre1'
    assert response.data[0]['description'] == 'description1'


@pytest.mark.django_db
def test_author_list(api_client, create_objects):
    response = api_client.get('/api/authors/')
    assert response.status_code == 200
    assert response.data[0]['name'] == 'author1'
    assert response.data[0]['biography'] == 'biography1'


@pytest.mark.django_db
def test_publisher_list(api_client, create_objects):
    response = api_client.get('/api/publishers/')
    assert response.status_code == 200
    assert response.data[0]['name'] == 'publisher1'
    assert response.data[0]['description'] == 'description1'
