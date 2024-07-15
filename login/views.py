from django.shortcuts import render
import json
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404

from django.contrib.auth import logout as django_logout
from decouple import config
from login.models import Profile,KarmaPoints
from django.http import Http404

def ProfileConfig(request):
    return render()
            
    
# Create your views here.
def index(request):
    user = request.user
    print(user)
    if user.is_authenticated:
        auth_0_user = user.social_auth.get(provider='auth0')
        user_id= auth_0_user.uid
        try:
            user_profile = Profile.objects.get(user_id=user_id)
        except Profile.DoesNotExist:
            user_profile = None
    else:
        user_id= None
        user_profile = None
    params={
        'user_ID':user_id,
        'user_profile':user_profile
        }
    return render(request,'index.html',params)

        

def profile(request):
    user=request.user
    if user.is_authenticated:
        auth_0_user = user.social_auth.get(provider='auth0')
        user_id= auth_0_user.uid
        try:
            user_profile = Profile.objects.get(user_id=user_id)
        except Profile.DoesNotExist:
            raise Http404("User profile does not exist")
        context={
            'user_profile':user_profile
        }
        return render(request, 'profile.html',context)
    else:
        raise Http404("User not logged in")
def logout(request):
    django_logout(request)
    domain= config("APP_DOMAIN")
    client_id = config("APP_CLIENTID")
    return_to = "http://localhost:8000"
    return HttpResponseRedirect (f"https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}")
def Create_Profile(request):
        
    
    user=request.user
    print(user)
    auth_0_user = user.social_auth.get(provider='auth0')
    user_id=auth_0_user.uid
    if Profile.objects.filter(user_id=user_id).exists():
        return redirect('/profile')
    if request.method=='POST':
        
        user=request.user
        print(user)
        auth_0_user = user.social_auth.get(provider='auth0')
        print("Error space 1")
        user_name=request.POST.get('name')
        user_email=request.POST.get('user-email')
        phone=request.POST.get('phone')
        print("Error space 2")
        profile, created=Profile.objects.get_or_create(user_id=user)
        print("Error space 3")
        profile.user_id=auth_0_user.uid
        profile.name=user_name
        profile.email=user_email
        profile.mobile=phone
        profile.KarmaPoints=profile.KarmaPoints+10
        profile.save()
        
        KarmaPoints.objects.create(user_id=auth_0_user.uid,karma_points=10,karma_points_type="Sign Up")
        
        return redirect('/profile')
    return render(request, 'Create_Profile.html')
def About(request):
    return render(request,'About.html')
    