from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from .permissions import CustomPermissionMixin
from .models import Book, BookInstances, Author, Genre, Publisher, Category
from .serializers import BookSerializer, BookInstanceSerializer, PublisherSerializer, GenreSerializer, AuthorSerializer, CategorySerializer


class BookViewSet(CustomPermissionMixin, ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookInstanceViewSet(CustomPermissionMixin, ModelViewSet):
    queryset = BookInstances.objects.all()
    serializer_class = BookInstanceSerializer


class AuthorViewSet(CustomPermissionMixin, ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(CustomPermissionMixin, ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PublisherViewSet(CustomPermissionMixin, ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class CategoryViewSet(CustomPermissionMixin, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
