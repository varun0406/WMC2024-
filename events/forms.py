# forms.py
from django import forms
from .models import Venue, Event, Organization

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['venue_name', 'venue_address', 'venue_contact', 'venue_capacity', 'image']

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['org_name', 'org_contact', 'org_email', 'org_desc']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_desc', 'event_s_time', 'event_e_time', 'venue', 'organization', 'Image1', 'Image2', 'Image3', 'Image4', 'Event_Tickets']
