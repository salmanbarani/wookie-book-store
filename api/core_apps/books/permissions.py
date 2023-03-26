from django.conf import settings
from rest_framework.permissions import BasePermission


class IsMemberOfBannedGroup(BasePermission):
    def has_permission(self, request, view):
        # user shouldn't be member of BannedGroup
        if request.user and request.user.is_authenticated:
            return not request.user.groups.filter(
                name=settings.BANNED_USERS_GROUP_NAME
            ).exists()
        return True
