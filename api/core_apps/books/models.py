from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.common.fields import PositiveDecimalField
from core_apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Book(TimeStampedUUIDModel):
    title = models.CharField(max_length=100, verbose_name=_("title"))
    description = models.TextField(verbose_name=_("description"))
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="books", verbose_name=_("author")
    )
    cover_image = models.ImageField(
        verbose_name=_("cover image"), default="/cover_default.png"
    )

    price = PositiveDecimalField(_("price"))

    def __str__(self) -> str:
        return self.title
