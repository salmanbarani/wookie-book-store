from django.contrib.auth import get_user_model
from django.test import TestCase

from core_apps.authors.models import Profile


class SignalsTestCase(TestCase):
    def test_profile_creation_signal(self):
        User = get_user_model()
        user = User.objects.create(
            email="test@example.com",
            password="password123",
            first_name="John",
            last_name="Doe",
        )

        profile = Profile.objects.filter(user=user).first()
        self.assertIsNotNone(profile)
        self.assertEqual(profile.user, user)
        self.assertEqual(profile.user.first_name, "John")
        self.assertEqual(profile.user.last_name, "Doe")
