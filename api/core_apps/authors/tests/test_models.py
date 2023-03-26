import pytest
from django.test import TestCase

from ..models import Profile


@pytest.mark.usefixtures("user")
class UserTests(TestCase):
    def test_profile_is_created_when_user_is_created(self):
        self.assertIsNotNone(self.user.profile)

    def test_making_sure_the_profile_has_correct_value(self):
        profile = self.user.profile

        self.assertEqual(profile.about_me, "")
        self.assertEqual(profile.gender, "other")

        about_me = "my name is Salman and I'm an engineer"
        gender = "male"

        profile.about_me = about_me
        profile.gender = gender
        profile.save()

        updated_profile = Profile.objects.get(user=self.user)

        self.assertEqual(updated_profile.about_me, about_me)
        self.assertEqual(updated_profile.gender, gender)
