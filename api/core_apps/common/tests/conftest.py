import pytest
from ..models import TimeStampedUUIDModel


@pytest.fixture(scope="class")
def sample_timestamped_uuid_model(request):
    pass
    # request.cls.sample_timestamped_uuid_model = DummyClass.objects.create()
