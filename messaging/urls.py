from django.urls import path
from .views import whatsapp_webhook
from .views import send_message


urlpatterns = [
    path('webhook/', whatsapp_webhook, name='whatsapp_webhook'),
    path('send/', send_message, name='send_message'),
]