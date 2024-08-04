from django.urls import path
from . import views
app_name = 'events'
urlpatterns = [
    path('administ/', views.admin_dashboard, name='admin_dashboard'),
    path('edit_venue/<int:venue_id>', views.edit_venue, name='edit_venue'),
    path('delete_venue/<int:venue_id>', views.delete_venue, name='delete_venue'),
    path('administ/edit_organization/<int:org_id>/', views.edit_organization, name='edit_organization'),
    path('administ/delete_organization/<int:org_id>/', views.delete_organization, name='delete_organization'),
    path('administ/edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('administ/delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('query/<int:query_id>/', views.query_details, name='query_details'),
    path('query/answered/<int:query_id>/', views.query_answered, name='query_answered'),
]
