from rest_framework import serializers
from rest_framework.relations import RelatedField

from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ("name",)


class BookInstanceSerializer(serializers.ModelSerializer):
    # publisher = RelatedField(queryset=Publisher.objects.all())
    publisher = serializers.CharField(source='publisher.name')

    class Meta:
        model = BookInstances
        fields = ('publisher', 'count')


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)
    book_instances = BookInstanceSerializer(many=True, read_only=True, source='price')
    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, instance):
        result = 0
        for price in instance.price.all():
            result += price.count
        return result


    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'genres', 'category', 'book_instances', 'total_amount')


class PriceSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=False)

    class Meta:
        model = BookInstances
        fields = ("book", "price",)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
