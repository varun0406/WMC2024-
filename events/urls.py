from django.urls import path,include
from . import views
app_name = 'events'
urlpatterns = [
    path("adminst/", views.admin, name="admin"),
]