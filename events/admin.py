from django.contrib import admin
from .models import Organization, Venue, Event,Question,Quiz

# Register models with the admin site
admin.site.register(Organization)
admin.site.register(Venue)
admin.site.register(Event)

# admin.site.register(Ticket)
admin.site.register(Question)
admin.site.register(Quiz)