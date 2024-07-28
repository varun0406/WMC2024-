from django.urls import path
from .consumers import AdminConsumer

websocket_urlpatterns = [
    path('ws/administrator',AdminConsumer.as_asgi()),
    path("ws/Donaters_Dashboard/<str:slug>/",AdminConsumer.as_asgi())
]
print(websocket_urlpatterns)
