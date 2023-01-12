# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


from .models import CartBook, Cart
from .serializers import CartBookSerializer, CartSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartBookViewSet(ModelViewSet):
    queryset = CartBook.objects.all()
    serializer_class = CartBookSerializer
