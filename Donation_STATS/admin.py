from django.contrib import admin

# Register your models here.
from .models import Donation,Statistics
admin.site.register(Donation)
admin.site.register(Statistics)

