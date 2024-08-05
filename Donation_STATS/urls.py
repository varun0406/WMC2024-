from django.urls import path
from .views import donate_main, Donaters_Dashboard,donaters,qdemo

app_name = 'Donation_STATS'

urlpatterns = [
    path('leaderboard/', donate_main, name='donate_main'),
    path('Donaters_Dashboard/<slug:slug>/', Donaters_Dashboard, name='Donaters_Dashboard'),
    path("donation",donaters,name="Donation"),
    path("qdemo",qdemo,name="qdemo")
]
