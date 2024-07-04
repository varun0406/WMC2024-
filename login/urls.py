from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile.html'),
    path("",include("social_django.urls"))    
]
