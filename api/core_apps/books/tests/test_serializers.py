import pytest
from django.test import TestCase

from ..serializers import BookSerializer


def get_fields_list():
    return ["pkid", "title", "description", "author", "price", "cover_image"]


@pytest.mark.usefixtures("book", "user")
class BookTests(TestCase):
    def setUp(self):
        self.serializer_data = {
            field: getattr(self.book, field) for field in get_fields_list()
        }
        self.serializer = BookSerializer(instance=self.book)

    def test_book_serializer_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(get_fields_list()))

    def test_book_serializer_author_is_user_full_name(self):
        self.assertEqual(self.serializer.data["author"], self.book.author.full_name)
