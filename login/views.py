from django.shortcuts import render
import json
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404

from django.contrib.auth import logout as django_logout
from decouple import config
from login.models import Profile,KarmaPoints,Transactions,UserQuery
from .models import Testimonial as test
from django.http import Http404
from events.models import Event,Venue,Organization,Ticket

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
    if request.method=='POST':
        full_name = request.POST.get('FirstName')
        email = request.POST.get('Email')
        query_msg=request.POST.get('message')
        user_query = UserQuery.objects.create(user_id=full_name, user_email=email, query=query_msg)
        # Print the created instance
        print(user_query)
        context = {**params, "alert": "Your Query is submitted, will answer in 24 hours!"}
        return render(request,'index.html',context)
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
    testi = test.objects.all()
    params={
        'user_ID':user_id,
        'user_profile':user_profile,
        'test':testi
        }
    return render(request,'About.html',params)

def Leaderboard(request):
    return render(request,'Lead.html')
def Donate_Ngo(request):
    return render(request,'NGO_Donation.html')


def Membership(request,alert=None):
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
    return render(request,'Membership.html',params)


def Events(request):
    events = Event.objects.all()
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

    print(user)  # This will print the User object or AnonymousUser instance

    if not user.is_authenticated:
        return render(request, "index.html", {"alert": "You need to log in first to access this page"})
    try:
        profile = Profile.objects.get(user_id=user)
        check_membership = profile.Membership_license

        if check_membership == "None":
            return render(request, "Membership.html", {"alert": "Please buy a membership to access this page"})
        
    except Profile.DoesNotExist:
        # Handle the case where the profile does not exist
        return render(request, "index.html", {"alert": "Profile not found. Please create a profile."})

    print(events)

    return render(request, 'Events.html', {'events': events,**params})
   
def Eventpage(request,slug):
    user = request.user
    print(user)
    if request.method == 'POST':
        # Extract data from POST request
        discount_amt = int(request.POST.get("membership"))
        total_price_paid = int(request.POST.get("pricet"))
        events = Event.objects.get(slug=slug)
        user_profile=Profile.objects.get(user_id=user.username)
        # Create the Ticket
        ticket = Ticket.objects.create(
            user_id=user_profile,
            event=events,
            discount=discount_amt,
            email=request.POST.get("email"),
            attendee_name=request.POST.get("full_name"),
            total_paid_price=total_price_paid,
            tickets=request.POST.get("ticket_number")
        )
        
        # Redirect or return response
        return redirect('/ticket/{}'.format(ticket.id))


        
        
    if user.is_authenticated:
          
        user_id= user.username
        try:
            user_profile = Profile.objects.get(user_id=user_id)
        except Profile.DoesNotExist:
            user_profile = None
        try:
            event = Event.objects.get(slug=slug)
            venue=Venue.objects.get(id=event.venue_id)
            org=Organization.objects.get(id=event.organization_id)
            discount=0
            membership=Profile.objects.get(user_id=user_id).Membership_license
            if membership=="Gold":
                discount=40
            elif membership=="Bronze":
                discount=15
            elif membership=="Silver":
                discount=10
           
            
        except Event.DoesNotExist:
            return HttpResponse("error not event exist",status=404)
    else:
        user_id= None
        user_profile = None
    
    params={
                'event':event,
                'venue':venue,
                'org':org,
                'user_ID':user_id,
                'user_profile':user_profile,
                "discount":discount
            }
    return render(request,'Eventpage.html',params)


def Membership_Buy(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, "index.html", {"alert": "You need to log in first to access this page"})
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
    if request.method=='POST':
        user=request.user
        user_id=str(user.username)
        print(request.POST)
        Karma_Available=Profile.objects.get(user_id=user_id).KarmaPoints
        print(Karma_Available)

        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        occupation = request.POST.get('occupation')
        dob_day = request.POST.get('dob_day')
        dob_month = request.POST.get('dob_month')
        dob_year = request.POST.get('dob_year')
        gender = request.POST.get('gender')
        terms = request.POST.get('terms')
        tier=request.POST.get('payment-method')
        if tier=="basic":
            if Karma_Available<100:
                return render(request, "index.html", {"alert": "You dont have enough karma points to buy our basic membership"})
            else:
                KarmaPoints.objects.create(user_id=user_id,karma_points=-100,karma_points_type="Basic Membership")
                Karma_Available=Karma_Available-100
        elif tier=="standard":
            if Karma_Available<500:
                return render(request, "index.html", {"alert": "You dont have enough karma points to buy our Standard membership"})
            else:
                KarmaPoints.objects.create(user_id=user_id,karma_points=-500,karma_points_type="Membership Tier Upgrade")
                Karma_Available=Karma_Available-500
        elif tier=="premium":
            if Karma_Available<2000:
                return render(request, "index.html", {"alert": "You dont have enough karma points to buy our Premium membership"})
            else:
                Karma_Available=Karma_Available-2000
        # Profile.objects.update(user_id=user_id,KarmaPoints=Karma_Available)
        profile=Profile.objects.get(user_id=user_id)
        print(Karma_Available)
        profile.KarmaPoints = Karma_Available
        profile.Membership_license = tier
        profile.save()
        return render(request,'index.html', {"alert": f"You successfully bought our {tier} membership.","params":params})
    return render(request,'Membership_Buy.html',params)


def Testimonial(request):
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
    
    if user.is_authenticated:
          
        user_id= user.username
        try:
            user_testimonial = test.objects.get(username=user_id)
        except test.DoesNotExist:
            if user_profile is None:
                user_testimonial="h"
            elif user_profile.Membership_license=="None":
                user_testimonial="h"
            else:
                user_testimonial=None
    else:
        user_testimonial="h"
    testi = test.objects.all()
    params={
        'user_ID':user_id,
        'user_profile':user_profile,
        'user_testimonial':user_testimonial,
        'test':testi
        }
    return render(request,'testimonials.html',params)
    
def Review(request):
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
    if request.method=='POST':
        Name= request.POST.get('name')
        occupation=request.POST.get('occupation')
        T_topic=request.POST.get('Review_topic')
        testimonial=request.POST.get('opinion')
        rati=request.POST.get('rating')
        print(Name,occupation,T_topic,testimonial)
        Testimo, created=test.objects.get_or_create(username=user_id)
        Testimo.Name=Name
        Testimo.Occupation=occupation
        Testimo.Testimonial_topic=T_topic
        Testimo.testimonial=testimonial
        Testimo.rating=rati
        print(rati)
        Testimo.save()
    return render(request,'review.html',params)


def Karma_Quiz(request):
    user = request.user
    if user.is_authenticated:
        user_id = user.username
        try:
            user_profile = Profile.objects.get(user_id=user_id)
        except Profile.DoesNotExist:
            user_profile = None
            return render(request, "Create_Profile.html", {"alert": "You need to log in first to access this page"})
    else:
        return render(request, "index.html", {"alert": "You need to log in first to access this page"})
    
    params = {
        'user_ID': user_id,
        'user_profile': user_profile
    }
    return render(request, 'quiz.html', params)


def ticket(request, ticket_id=None):
    user=request.user
    if user.is_authenticated:
        user_id=user.username
        user_profile=Profile.objects.get(user_id=user_id)
        ticket_data=get_object_or_404(Ticket, id=ticket_id)
        event_data=Event.objects.get(id=ticket_data.event.id)
        venue_data=Venue.objects.get(id=event_data.venue.id)
        
        params={
            "ticket":ticket_data,
            "venue":venue_data,
            "event":event_data
        }
        return render(request,"ticket.html",params)
    

