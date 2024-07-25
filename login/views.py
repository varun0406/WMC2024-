from django.shortcuts import render
import json
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404

from django.contrib.auth import logout as django_logout
from decouple import config
from login.models import Profile,KarmaPoints,Transactions
from django.http import Http404


def MemberShip_tier(request):
    if request.method=='POST':
        user=request.user
        user_id=user.username
        print(request.POST)
        tier=request.POST.get('membership-tier')
        Karma_Available=Profile.objects.get(user_id=user_id)
        print(Karma_Available)
        if tier=="Gold":
            if Karma_Available<100:
                return HttpResponse("Not enough Karma Points")
            else:
                KarmaPoints.objects.create(user_id=user_id,karma_points=-100,karma_points_type="Membership Tier Upgrade")
                Karma_Available=Karma_Available-100
        elif tier=="Silver":
            if Karma_Available<50:
                return HttpResponse("Not enough Karma Points")
            else:
                KarmaPoints.objects.create(user_id=user_id,karma_points=-50,karma_points_type="Membership Tier Upgrade")
                Karma_Available=Karma_Available-50
        elif tier=="Bronze":
            if Karma_Available<10:
                return HttpResponse("Not enough Karma Points")
            else:
                Karma_Available=Karma_Available-10
        KarmaPoints.objects.create(user_id=user_id,karma_points=-10,karma_points_type="Membership Tier Upgrade")
        Profile.objects.update(user_id=user_id,KarmaPoints=Karma_Available)
        profile=Profile.objects.get(user_id=user_id)
        profile.Membership_tier=tier
        profile.save()
    return render(request,'Membership_tier.html')

            
    
# Create your views here.
def index(request):
    user = request.user
    print(user)
    if user.is_authenticated:
          
        user_id= user.username
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
    
        user_id= user.username
        try:
            user_profile = Profile.objects.get(user_id=user_id)
        except Profile.DoesNotExist:
            raise Http404("User profile does not exist")
        karma=KarmaPoints.objects.filter(user_id=user_id)
        trans=Transactions.objects.filter(payer_id=user_id)
        context={
            'user_profile':user_profile,
            'karma_points':karma,
            'Transactions':trans
        }
        print(context)
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

    user_id=user.username
    if Profile.objects.filter(user_id=user_id).exists():
        return redirect('/profile')
    if request.method=='POST':
        
        user=request.user
      
        print("Error space 1")
        user_name=request.POST.get('name')
        user_email=request.POST.get('user-email')
        phone=request.POST.get('phone')
        print("Error space 2")
        profile, created=Profile.objects.get_or_create(user_id=user)
        print("Error space 3")
        profile.user_id=user.username
        profile.name=user_name
        profile.email=user_email
        profile.mobile=phone
        profile.KarmaPoints=profile.KarmaPoints+10
        profile.save()
        
        KarmaPoints.objects.create(user_id=user.username,karma_points=10,karma_points_type="Sign Up")
        return redirect('/profile')
    return render(request, 'Create_Profile.html')

def About(request):
    return render(request,'About.html')

def Leaderboard(request):
    return render(request,'Lead.html')
def Donate_Ngo(request):
    return render(request,'NGO_Donation.html')
def Membership(request):
    return render(request,'Membership.html')
def Events(request):
    return render(request,'Events.html')
def Eventpage(request):
    return render(request,'Eventpage.html')
    
    