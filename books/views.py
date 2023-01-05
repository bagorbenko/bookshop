from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Book, BookInstance
from .serializers import BookSerializer, PriceSerializer



class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class PriceAPIView(generics.ListAPIView):
    queryset = BookInstance.objects.all()
    serializer_class = PriceSerializer
