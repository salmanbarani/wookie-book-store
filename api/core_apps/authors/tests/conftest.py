import pytest

from core_apps.users.factories import UserFactory


@pytest.fixture(scope="class")
def user(request):
    request.cls.user = UserFactory()


@pytest.fixture(scope="class")
def list_of_users(request):
    UserFactory.create_batch(size=20)
