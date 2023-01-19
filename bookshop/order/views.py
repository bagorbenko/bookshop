from rest_framework import mixins, viewsets
from .models import Order
from .serializers import OrderSerializer


class OrderAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

