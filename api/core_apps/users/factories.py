from django.conf import settings
import factory
import pytz
from faker import Faker

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "dolphins")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    class Meta:
        model = settings.AUTH_USER_MODEL
        django_get_or_create = ("email",)


class StaffUserFactory(UserFactory):
    is_staff = True


class AdminUserFactory(StaffUserFactory):
    is_admin = True
