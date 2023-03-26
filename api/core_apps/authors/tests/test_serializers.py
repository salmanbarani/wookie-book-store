import pytest
from django.test import TestCase

from ..serializers import ProfileSerializer, UpdateProfileSerializer


@pytest.mark.usefixtures("user")
class ProfileSerializerTestCase(TestCase):
    def test_profile_serializer_returns_expected_fields(self):
        serializer = ProfileSerializer(self.user.profile)
        expected_fields = [
            "username",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "id",
            "profile_photo",
            "about_me",
            "gender",
            "twitter_handle",
        ]
        self.assertCountEqual(serializer.data.keys(), expected_fields)

    def test_profile_serializer_returns_correct_full_name(self):
        serializer = ProfileSerializer(self.user.profile)
        self.assertEqual(serializer.data["first_name"], self.user.first_name)
        self.assertEqual(serializer.data["last_name"], self.user.last_name)
        self.assertEqual(serializer.data["gender"], self.user.profile.gender)


@pytest.mark.usefixtures("user")
class UpdateProfileSerializerTestCase(TestCase):
    def test_update_profile_serializer_returns_expected_fields(self):
        serializer = UpdateProfileSerializer(instance=self.user.profile)
        expected_fields = [
            "username",
            "first_name",
            "last_name",
            "profile_photo",
            "about_me",
            "gender",
            "twitter_handle",
        ]
        self.assertCountEqual(serializer.data.keys(), expected_fields)

    def test_update_profile_serializer_fields_are_read_only(self):
        serializer = UpdateProfileSerializer(
            instance=self.user.profile, data={"username": "newusername"}
        )
        self.assertTrue(serializer.is_valid())
        self.assertFalse(serializer.fields["username"].write_only)
        self.assertTrue(serializer.fields["username"].read_only)
        self.assertEqual(serializer.validated_data, {})
