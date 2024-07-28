from django.urls import path
from .donaters import LeaderboardConsumer,DashBoard
websocket_urlpatterns = [
    path('ws/leaderboard/', DashBoard.as_asgi()),
    path('ws/Donaters_Dashboard/<str:slug>/', DashBoard.as_asgi()),
]
