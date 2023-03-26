import pytest
from django.test import TestCase

from ..models import User


@pytest.mark.usefixtures("user")
class UserFactoryTestCase(TestCase):
    def test_user_created(self):
        self.assertIsNotNone(self.user)

    def test_user_stored_on_db(self):
        self.assertTrue(User.objects.filter(pkid=self.user.pkid).exists())

    def test_user_stored_correct_value(self):
        not_none_fields = ["first_name", "last_name", "email"]
        for field in not_none_fields:
            self.assertIsNotNone(getattr(self.user, field))
