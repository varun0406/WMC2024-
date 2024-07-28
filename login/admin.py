from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile,KarmaPoints,Transactions,UserQuery

admin.site.register(Profile)
admin.site.register(KarmaPoints)
admin.site.register(Transactions)
admin.site.register(UserQuery)
