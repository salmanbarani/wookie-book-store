from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthorsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.authors"
    verbose_name = _("Authors")

    def ready(self):
        from core_apps.authors import signals
