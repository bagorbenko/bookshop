from rest_framework.viewsets import ModelViewSet

from .models import CartItem, Cart
from .serializers import CartBookSerializer, CartSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartBookViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartBookSerializer

