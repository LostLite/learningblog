from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #import the defined signals
    def ready(self):
        from . import signals
