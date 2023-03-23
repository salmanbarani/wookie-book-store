from django.test import TestCase
import pytest
from core_apps.users import factories, models


def sample_user_data():
    return {
        "first_name": factories.UserFactory.first_name,
        "last_name": factories.UserFactory.last_name,
        "username": factories.UserFactory.last_name,
        "email": factories.UserFactory.build().email,
        "password": models.User.objects.make_random_password()
    }


class CustomUserTests(TestCase):
    def test_create_user(self):

        sample_data = sample_user_data()
        user = models.User.objects.create_user(**sample_data)

        self.assertEqual(user.email, sample_data["email"])
        self.assertTrue(user.check_password(sample_data["password"]))

    def test_create_user_error(self):
        bad_data = sample_user_data()
        bad_data["email"] = ""

        with self.assertRaises(ValueError):
            models.User.objects.create_user(**bad_data)

    def test_create_superuser(self):
        super_user_data = sample_user_data()
        user = models.User.objects.create_superuser(
            **super_user_data
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.check_password(super_user_data["password"]))
