from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import (
    BookViewSet,
    PriceViewSet,
    GenreViewSet,
    AuthorViewSet,
    PublisherViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register(r'books', BookViewSet, basename="books")
router.register(r'prices', PriceViewSet, basename="prices")
router.register(r'authors', AuthorViewSet, basename="author")
router.register(r'genres', GenreViewSet, basename="genres")
router.register(r'publishers', PublisherViewSet, basename="publishers")
router.register(r'category', CategoryViewSet, basename="category")


urlpatterns = [
    path('api/', include(router.urls)),
]

urlpatterns += router.urls
