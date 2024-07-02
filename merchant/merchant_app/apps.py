from django.apps import AppConfig


class MerchantAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'merchant_app'
    
    def ready(self):
        from . import signals  # Import signals to connect them