from django.core.exceptions import PermissionDenied


class BannedUserCantPublishBook(PermissionDenied):
    pass
