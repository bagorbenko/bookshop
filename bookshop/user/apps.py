from django.apps import AppConfig


default_app_config = 'user.apps.AppConfig'

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
