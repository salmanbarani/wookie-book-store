import pytest
from core_apps.users.factories import UserFactory


@pytest.fixture(scope="class")
def user(request):
    request.cls.user = UserFactory()
