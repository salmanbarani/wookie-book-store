import pytest
from core_apps.users.factories import UserFactory
from django.contrib.auth.models import Group
from .. import factories
from django.conf import settings


@pytest.fixture(scope="class")
def book(request):
    request.cls.book = factories.BookFactory()


@pytest.fixture(scope="class")
def books(request):
    factories.BookFactory.create_batch(size=30)


@pytest.fixture(scope="class")
def user(request):
    request.cls.user = UserFactory()


@pytest.fixture(scope="class")
def banned_user(request):
    user = UserFactory()
    group = Group.objects.create(name=settings.BANNED_USERS_GROUP_NAME)
    user.groups.add(group)
    user.save()
    request.cls.banned_user = user
