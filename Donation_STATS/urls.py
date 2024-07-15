from django.urls import path
from .views import donate_main, Donaters_Dashboard

app_name = 'Donation_STATS'

urlpatterns = [
    path('donate_main/', donate_main, name='donate_main'),
    path('Donaters_Dashboard/<slug:slug>/', Donaters_Dashboard, name='Donaters_Dashboard'),
]
