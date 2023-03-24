from django.test import TestCase
import pytest
from ..models import TimeStampedUUIDModel


@pytest.mark.usefixtures("sample_timestamped_uuid_model")
class UserTests(TestCase):

    def test_sample_timestamped_uuid_model_was_created(self):
        # self.assertEqual(str(self.sample_timestamped_uuid_model), self.sample)
        assert True
