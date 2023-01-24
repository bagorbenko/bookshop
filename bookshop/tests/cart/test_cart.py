import pytest
from django.contrib.auth import get_user_model
from rest_framework import status


@pytest.mark.django_db
class TestsCart:
    endpoint = "/api/registration/"

    def test_create_cart(self, api_client, user_data):
        response = api_client.post(
            self.endpoint,
            data=user_data,
            format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED
        user = get_user_model().objects.get(username=user_data["username"])
        assert user.cart

