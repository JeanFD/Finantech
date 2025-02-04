from django.apps import AppConfig

class FinantechConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'finantech'

    def ready(self):
        import finantech.signals