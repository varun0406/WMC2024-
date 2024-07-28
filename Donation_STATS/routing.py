from django.urls import path
from .donaters import LeaderboardConsumer

websocket_urlpatterns = [
    path('ws/leaderboard/', LeaderboardConsumer.as_asgi()),
]
