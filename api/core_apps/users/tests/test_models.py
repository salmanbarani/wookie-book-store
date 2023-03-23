from django.test import TestCase

import pytest


@pytest.mark.usefixtures("user")
class UserTests(TestCase):
    def test_user_returns_full_name(self):
        self.assertEqual(str(self.user), self.user.full_name)
