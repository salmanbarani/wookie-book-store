from django.test import TestCase
from rest_framework.test import APIClient
import pytest
from rest_framework import status
from ..models import Book
from core_apps.users.factories import UserFactory

PROFILE_LIST_URL = "/api/v1/profiles/all/"
PROFILE_DETAIL_URL = "/api/v1/profiles/user/"
PROFILE_UPDATE_URL = "/api/v1/profiles/update/"

PAGE_SIZE = 5

BOOK_URL = '/api/v1/books/'


def get_payload(user, title="title", description="description", price="55.50"):
    return {
        "author": user,
        "title": title,
        "description": description,
        "price": price
    }


def add_books_to_user(user, size=3):
    for book in Book.objects.all()[:3]:
        book.author = user
        book.save()
    return Book.objects.filter(author=user).count()


@pytest.mark.usefixtures("user", "banned_user", "book", "books")
class UserAuthenticationTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.private_client = APIClient()
        self.private_client.force_authenticate(self.user)

    def test_get_list_of_books(self):
        response = self.client.get(BOOK_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), PAGE_SIZE)

    def test_get_book_detail(self):
        book_id = self.book.pkid
        response = self.client.get(f"{BOOK_URL}{book_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        book_title = self.book.title
        response_title = response.json()['title']
        self.assertEqual(book_title, response_title)

    def test_publish_not_authenticated_book(self):
        response = self.client.post(BOOK_URL, get_payload(self.user))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_plublish_book_mission_data(self):
        payload = get_payload(self.user, title="")
        response = self.private_client.post(BOOK_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_publish_book_ban_group(self):
        payload = get_payload(self.banned_user)
        banned_user_client = APIClient()
        banned_user_client.force_authenticate(self.banned_user)
        response = banned_user_client.post(BOOK_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_publish_book_successful(self):
        payload = get_payload(self.user)
        payload.pop('author')

        response = self.private_client.post(BOOK_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        for key in payload:
            self.assertEqual(payload[key], response.json()[key])
        self.assertEqual(self.user.full_name, response.json()['author'])

    def test_unpublish_not_owner_book(self):
        client = APIClient()
        client.force_authenticate(UserFactory())
        response = client.delete(f"{BOOK_URL}{self.book.pkid}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unpublish_book(self):
        client = APIClient()
        client.force_authenticate(self.book.author)
        response = client.delete(f"{BOOK_URL}{self.book.pkid}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_not_owner_book(self):
        client = APIClient()
        client.force_authenticate(UserFactory())
        response = client.patch(f"{BOOK_URL}{self.book.pkid}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_bad_book_data(self):
        payload = get_payload(self.user)
        payload['price'] = "asdfasdf"
        client = APIClient()
        client.force_authenticate(self.book.author)
        response = client.patch(f"{BOOK_URL}{self.book.pkid}/", data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_book_not_found(self):
        payload = get_payload(self.user)
        client = APIClient()
        client.force_authenticate(self.book.author)
        response = client.patch(f"{BOOK_URL}pkid-not-exist/", data=payload)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def update_success(self):
        payload = get_payload(self.user)
        client = APIClient()
        client.force_authenticate(self.book.author)
        response = client.patch(f"{BOOK_URL}{self.book.pkid}/", data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for key in payload:
            self.assertEqual(payload[key], response.json()[key])

    def test_search_by_filter(self):

        user_books = add_books_to_user(self.user)
        filter_fields = {
            "format": "json",
            "author__first_name": self.user.first_name,
            "author__last_name": self.user.last_name,
        }
        response = self.client.get(BOOK_URL, filter_fields)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), user_books)
