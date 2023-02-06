from django.db import transaction
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from cart.permissions import IsOwnerOrReadOnly
from .models import Order
from .serializers import OrderSerializer


class OrderAPIView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet
                   ):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user.id)
