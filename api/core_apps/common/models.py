import uuid

from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models


class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]


def create_groups():
    # Specifing BannedUsers group to restrict some bad users like "_Darth Vader_"
    Group.objects.get_or_create(name=settings.BANNED_USERS_GROUP_NAME)
