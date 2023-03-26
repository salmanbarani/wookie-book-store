import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase

from ..serializers import CreateUserSerializer

User = get_user_model()


@pytest.mark.usefixtures("user")
class UserSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.serializer = CreateUserSerializer(
            data={
                "username": "johndoe",
                "email": "johndoe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "password": "ASDFasdfa345#$%",
            }
        )

    def test_user_serializer(self):
        self.assertTrue(self.serializer.is_valid())

    def test_serializer_store_data(self):
        self.serializer.is_valid()
        self.serializer.save()
        self.assertTrue(User.objects.filter(username="johndoe").exists())
