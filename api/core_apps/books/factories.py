from django.conf import settings
import factory
from faker import Faker
from .models import Book
from decimal import Decimal

fake = Faker()


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Sequence(lambda n: f'Title {n}')
    description = factory.Faker('paragraph')
    author = factory.SubFactory(settings.AUTH_USER_FACTORY)
    price = Decimal('19.99')
