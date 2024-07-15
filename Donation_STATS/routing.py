from django.urls import path
from .donaters import DashBoard

websocket_urlpatterns = [
    path('ws/Donaters_Dashboard/<str:slug>/', DashBoard.as_asgi()),
]
