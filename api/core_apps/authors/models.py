from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Profile(TimeStampedUUIDModel):
    """
        Author profile
    """
    class Gender(models.TextChoices):
        MALE = "male", _("male")
        FEMALE = "female", _("female")
        OTHER = "other", _("other")

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    about_me = models.TextField(
        verbose_name=_("about me"),
        default="",
    )
    gender = models.CharField(
        verbose_name=_("gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )

    profile_photo = models.ImageField(
        verbose_name=_("profile photo"), default="/profile_default.png"
    )

    twitter_handle = models.CharField(
        verbose_name=_("twitter_handle"), max_length=20, blank=True
    )

    def __str__(self):
        return f"{self.user.full_name}'s profile"
