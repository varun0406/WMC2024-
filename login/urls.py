from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile.html'),
    path("",include("social_django.urls")),
    path('logout', views.logout, name='logout'),
    path('Create_Profile', views.Create_Profile, name='Create_Profile'),
    path('About', views.About, name='About'),
    path('Membership', views.Membership, name='Membership'),

    path("member",views.MemberShip_tier,name="MemberShip_tier"),
    path("Events",views.Events,name="Events"),
    path('Eventpage/<slug:slug>/', views.Eventpage, name='Eventpage'),
    path("Membership_Buy",views.Membership_Buy,name="Events"),

]
