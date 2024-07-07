from django.shortcuts import render
import json
from django.http import HttpResponseRedirect

from django.contrib.auth import logout as django_logout
from decouple import config
from login.models import Profile
from django import forms

def ProfileConfig(request):
    form =forms(Profile)
    
            
    
# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    user = request.user
    auth_0_user = user.social_auth.get(provider='auth0')
    user_data= {
        'user_id': auth_0_user.uid,
        "name": user.first_name,
        "email": user.email,
        "picture": auth_0_user.extra_data['picture']}
    context ={
        "user_data": user_data,
        "auth_0_user": auth_0_user,
        
    }
    print(context)
    return render(request, 'profile.html', context)
def logout(request):
    django_logout(request)
    domain= config("APP_DOMAIN")
    client_id = config("APP_CLIENTID")
    return_to = "http://localhost:8000"
    return HttpResponseRedirect (f"https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}")
    