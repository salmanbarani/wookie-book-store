from django.test import TestCase
from rest_framework.test import APIClient
import pytest
from core_apps.users.factories import UserFactory
from rest_framework import status
from ..models import Profile
import json

PROFILE_LIST_URL = "/api/v1/profiles/all/"
PROFILE_DETAIL_URL = "/api/v1/profiles/user/"
PROFILE_UPDATE_URL = "/api/v1/profiles/update/"

PAGE_SIZE = 4


@pytest.mark.usefixtures("user", "list_of_users")
class UserAuthenticationTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.private_client = APIClient()
        self.private_client.force_authenticate(self.user)
        self.bad_payload = {"first_name": "_Darth", "last_name": "Vader_"}
        self.payload = {"about_me": "about me was changed", "twitter_handle": "twittler.com//handler"}

    def test_get_list_of_profiles(self):
        response = self.client.get(PROFILE_LIST_URL).json()
        self.assertEqual(response["status_code"], status.HTTP_200_OK)
        self.assertEqual(PAGE_SIZE, len(response["profiles"]))

    def test_get_profile_detail(self):
        response = self.client.get(f"{PROFILE_DETAIL_URL}{self.user.username}/").json()
        self.assertEqual(response["status_code"], status.HTTP_200_OK)
        self.assertEqual(response["profile"]["username"], self.user.username)

    def test_profile_update_not_authentication_fail(self):
        response = self.client.patch(f"{PROFILE_UPDATE_URL}",
                                     self.bad_payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_profile_update_not_working_for_user_model_fields(self):
        user_info = {"first_name": self.user.first_name, "last_name": self.user.last_name}
        response = self.private_client.patch(f"{PROFILE_UPDATE_URL}",
                                             self.bad_payload).json()
        self.assertEqual(response["status_code"], status.HTTP_200_OK)

        for key in user_info.keys():
            self.assertEqual(user_info[key], response['profile'][key])

    def test_profile_update_success_for_profile_fields(self):

        for key in self.payload.keys():
            self.assertNotEqual(self.payload[key], getattr(self.user.profile, key))

        response = self.private_client.patch(f"{PROFILE_UPDATE_URL}",
                                             self.payload).json()
        self.assertEqual(response["status_code"], status.HTTP_200_OK)
        for key in self.payload.keys():
            self.assertEqual(self.payload[key], response['profile'][key])
