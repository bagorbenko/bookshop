from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


class OrderAPIView(mixins.ListModelMixin,
                   viewsets.GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user.id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        cart = self.request.user.cart
        serializer.save(cart=cart)
        cart.cart_items.all().delete()
