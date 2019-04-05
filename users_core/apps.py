from django.apps import AppConfig


class UsersCoreConfig(AppConfig):
    name = 'users_core'

    def ready(self):
        from . import singals