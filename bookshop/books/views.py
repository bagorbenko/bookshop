from rest_framework import mixins, viewsets
from .models import Book, BookInstance, Author, Genre, Publisher, Category
from .serializers import BookSerializer, BookInstanceSerializer, PublisherSerializer, GenreSerializer, AuthorSerializer, CategorySerializer


class BookAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookInstanceAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer


class AuthorAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PublisherAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class CategoryAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
