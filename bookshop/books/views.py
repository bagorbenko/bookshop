from rest_framework.viewsets import ModelViewSet

from .models import Book, BookInstances, Author, Genre, Publisher, Category
from .serializers import BookSerializer, PriceSerializer, PublisherSerializer, GenreSerializer, AuthorSerializer, CategorySerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PriceViewSet(ModelViewSet):
    queryset = BookInstances.objects.all()
    serializer_class = PriceSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
