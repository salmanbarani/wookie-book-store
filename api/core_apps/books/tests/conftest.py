import pytest

from .. import factories


@pytest.fixture(scope="class")
def book(request):
    request.cls.book = factories.BookFactory()
