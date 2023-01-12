from rest_framework import serializers
from .models import Cart, CartBook


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartBook
        fields = "__all__"