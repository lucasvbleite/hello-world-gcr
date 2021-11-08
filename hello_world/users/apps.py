from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "hello_world.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import hello_world.users.signals  # noqa F401
        except ImportError:
            pass
