from rest_framework import serializers
from .models import Book, BookInstances, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name", "biography", "image")


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('title', 'author',)


class PriceSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=False)

    class Meta:
        model = BookInstances
        fields = ('price', 'book')
