from django.apps import AppConfig


class HacknewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Hacknews'

#this function overides django's app on start feature.
    def ready(self):
        from . import updater

        updater.start()

