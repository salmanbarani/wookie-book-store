from django.test import TestCase, client
import pytest
from ..models import User
from rest_framework import status

JWT_PATH = "/api/v1/auth/jwt/create/"


@pytest.mark.usefixtures("user")
class UserAuthenticationTests(TestCase):
    def setUp(self) -> None:
        self.client = client.Client()
        self.user_data = {
            "username": "Soltan",
            "email": "soltan@gmail.com",
            "first_name": "soltan",
            "last_name": "solaiman",
            "password": "SEpass1234",
        }

    def test_successful_authentication(self):
        User.objects.create_user(**self.user_data)
        response = self.client.post(JWT_PATH, self.user_data)  # only email and password needed

        self.assertEqual(response.status_code, status.HTTP_200_OK)
