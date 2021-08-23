from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    import checkout.signals
