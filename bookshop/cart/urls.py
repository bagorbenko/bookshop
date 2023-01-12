from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartBookViewSet


router = DefaultRouter()
router.register(r'carts', CartViewSet, basename="carts")
router.register(r'cartbooks', CartBookViewSet, basename="cartbook")

urlpatterns = [
    path('api/', include(router.urls)),
]

urlpatterns += router.urls