from rest_framework import serializers
from .models import Book, BookInstance, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('title', 'author',)


class PriceSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=False)

    class Meta:
        model = BookInstance
        fields = ('price', 'book')
