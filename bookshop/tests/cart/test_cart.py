import pytest
from django.contrib.auth import get_user_model
from rest_framework import status

from cart.models import Cart
from tests.factories import BookInstanceFactory
from tests.factories import UserFactory, CartItemFactory


@pytest.mark.django_db
class TestsCart:
    endpoint = "/api/registration/"
    endpoint_cart = "/api/carts/"

    def test_create_cart(self, api_client, user_data):
        response = api_client.post(
            self.endpoint,
            data=user_data,
            format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED
        user = get_user_model().objects.get(username=user_data["username"])
        assert user.cart

    def test_add_book_to_cart(self, api_client):
        user = UserFactory()
        api_client.force_authenticate(user)
        cart = user.cart
        book = BookInstanceFactory(count=3)
        cart_item = CartItemFactory(cart=cart, book_instance=book, count=2)
        response = api_client.post(
            f"{self.endpoint_cart}/{user.id}",
            data={'cart_item_id': cart_item.id},
            format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['cart_item_id'] == cart_item.id
        assert response.data['count'] == 1
        assert Cart.objects.get(id=cart.id).books.count() == 1

