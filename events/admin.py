from django.contrib import admin
from .models import Organization, Venue, Event,  Ticket

# Register models with the admin site
admin.site.register(Organization)
admin.site.register(Venue)
admin.site.register(Event)

admin.site.register(Ticket)
