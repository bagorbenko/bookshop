from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


from .models import Book, BookInstances
from .serializers import BookSerializer, PriceSerializer


class BookAPIView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PriceAPIView(ModelViewSet):
    queryset = BookInstances.objects.all()
    serializer_class = PriceSerializer


