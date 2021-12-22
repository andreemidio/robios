from django.apps import AppConfig


class ProducaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.producao'

#https://stackoverflow.com/questions/68477402/listen-to-mqtt-topics-with-django-channels-and-celery
