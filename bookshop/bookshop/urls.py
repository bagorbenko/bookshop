from django.contrib import admin
from django.contrib.auth import login
from django.http import HttpResponse
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from books.views import *
from cart.views import CartAPIView, CartBookAPIView
from user.models import User
from user.views import UserAPIView, RegistrationAPIView
from order.views import OrderAPIView
from .yasg import urlpatterns as doc_urls


router = DefaultRouter()
router.register(r'books', BookAPIView, basename="books")
router.register(r'authors', AuthorAPIView, basename="author")
router.register(r'genres', GenreAPIView, basename="genres")
router.register(r'publishers', PublisherAPIView, basename="publishers")
router.register(r'categories', CategoryAPIView, basename="categories")
router.register(r'books_instances', BookInstanceAPIView, basename="books_instances")
router.register(r'carts', CartAPIView, basename="carts")
router.register(r'cartbooks', CartBookAPIView, basename="cartbooks")
router.register(r'users', UserAPIView, basename="users")
router.register(r'orders', OrderAPIView, basename="orders")


urlpatterns = [
    path('admin/', admin.site.urls, ),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path(r'api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/registration/', RegistrationAPIView.as_view(), name='registration')
]

urlpatterns += doc_urls
