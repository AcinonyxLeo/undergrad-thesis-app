from django.urls import path
from .views import LoRaView

urlpatterns = [
    path('gps/', LoRaView.as_view({
        'get':'loralist',
        'post':'loraread'
    }))
]