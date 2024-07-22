from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile.html'),
    path("",include("social_django.urls")),
    path('logout', views.logout, name='logout'),
    path('Create_Profile', views.Create_Profile, name='Create_Profile'),
    path('About', views.About, name='About'),
    path('Leaderboard', views.Leaderboard, name='Leaderboard'),
    path('Donate_Ngo', views.Donate_Ngo, name='Donate_Ngo'),
    path("member",views.MemberShip_tier,name="MemberShip_tier"),
]
