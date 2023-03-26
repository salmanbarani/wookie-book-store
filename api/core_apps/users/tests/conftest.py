import pytest
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .. import factories


@pytest.fixture(scope="class")
def user(request):
    request.cls.user = factories.UserFactory()


@pytest.fixture(scope="class")
def password(request):
    request.cls.password = get_user_model().objects.make_random_password()


@pytest.fixture(scope="class")
def uid(request, user):
    request.cls.uid = urlsafe_base64_encode(
        force_bytes(request.cls.user.email),
    )
