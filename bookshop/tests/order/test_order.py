import json
import pytest
from django.urls import reverse
from rest_framework import status

from books.models import BookInstance
from cart.models import CartItem, Cart
from order.models import Order
from tests.order.factories import UserFactory, CartFactory, CartItemFactory, OrderFactory


@pytest.mark.django_db
def test_cart_items_delete_after_order_creation(api_client):
    user = UserFactory()
    cart = user.cart
    cart_item = CartItemFactory(cart=cart, count=2)
    assert CartItem.objects.count() == 1
    url = "/api/orders/"
    data = {
        "user": user.id,
        "cart": cart.id
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert CartItem.objects.count() == 0
    assert Order.objects.count() == 1
    assert Order.objects.filter(user=user, cart=cart).exists()
    assert CartItem.objects.count() == 0


@pytest.mark.django_db
def test_user_can_see_their_own_orders(api_client):
    user = UserFactory()
    cart = user.cart
    order = OrderFactory(cart=cart)
    api_client.force_authenticate(user=user)
    response = api_client.get('/api/orders/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['id'] == order.id
    assert 'created_at' in response.data[0]
    assert 'updated_at' in response.data[0]