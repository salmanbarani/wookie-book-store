import factory
from django.conf import settings
from faker import Faker

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "dolphins")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.LazyAttribute(lambda obj: obj.email)

    class Meta:
        model = settings.AUTH_USER_MODEL
        django_get_or_create = ("email",)


class StaffUserFactory(UserFactory):
    is_staff = True


class AdminUserFactory(StaffUserFactory):
    is_admin = True
