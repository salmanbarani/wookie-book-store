from django.test import TestCase
from decimal import Decimal
import pytest


@pytest.mark.usefixtures("book")
class BookTests(TestCase):
    def test_book_is_created(self):
        self.assertEqual(str(self.book), self.book.title)

    def test_price_format_is_decimal(self):
        self.assertIsInstance(self.book.price, Decimal)
