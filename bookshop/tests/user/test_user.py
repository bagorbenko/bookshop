import pytest
from django.contrib.auth import get_user_model
from rest_framework import status

from tests.order.factories import UserFactory


@pytest.mark.django_db
class TestsUser:
    endpoint_registration = "/api/registration/"
    endpoint_login = "/api/drf-auth/login/"

    def test_create_user(self, api_client, user_data):
        expected_json = user_data
        response = api_client.post(
            self.endpoint_registration,
            data=expected_json,
            format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert get_user_model().objects.filter(username="testuser").exists()

    def test_user_can_login(self, api_client):
        password = 'testpassword'
        user = UserFactory(password=password)
        response = api_client.post(self.endpoint_login, {'username': user.username, 'password': password})
        assert response.status_code == status.HTTP_200_OK
