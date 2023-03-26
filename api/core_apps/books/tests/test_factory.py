import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase

from ..factories import BookFactory
from ..models import Book

User = get_user_model()


@pytest.mark.usefixtures("book", "user")
class BookFactoryTestCase(TestCase):
    def test_book_factory(self):
        self.assertTrue(Book.objects.filter(pkid=self.book.pkid))

    def test_book_factory_sequence(self):
        BookFactory.create_batch(size=4)
        self.assertEqual(Book.objects.count(), 5)  # 4 + 1 (in conftest file)
