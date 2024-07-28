from django.shortcuts import render,redirect,get_object_or_404
from .models import Donation,Statistics
from login.models import Transactions,KarmaPoints,Profile
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# Create your views here.

from django.shortcuts import render
from .models import Statistics, Donation

def donaters(request):
    user_id = request.user
    if request.method == "POST":
        
        user_id = request.user
        UserName = user_id.username
        FullName = request.POST.get('donation_description')     
        
        Donation_amount = int(request.POST.get('donation_amount'))
        donation_category = 'Karma_Foundation'
        donation_description = request.POST.get('donation_description')
        print(Donation_amount)
        
        print("error point 1")
        obj, created = Statistics.objects.get_or_create(Donaters_UserID=UserName, Name=FullName, defaults={'value': 0, 'ranking': 0})
        if created:
            obj.value = Donation_amount
        else:
            print(obj.value)
            obj.value += Donation_amount

        obj.save()
        print("error point 2")
        # Create a new Donation record
        # create code for transaction
        payer_id = UserName
        payee_id = "admin"
        transaction_type = "Donation"
        transaction_amount = Donation_amount
        transaction_obj = Transactions.objects.create(
            payer_id=payer_id,
            payee_id=payee_id,
            transaction_type=transaction_type,
            transaction_amount=transaction_amount
        )
        transaction_obj.save()
        # create code for karma points
        karma_points_obj, karma_points_created = KarmaPoints.objects.get_or_create(
            user_id=payer_id,
            karma_points_type="Donation",
            karma_points=(Donation_amount),
            reference_id=transaction_obj.transaction_id
        )
        karma_points_obj.save()
        
        # create code for Donation
        donation_obj = Donation.objects.create(
            UserID=UserName,
            user_name=obj,  # Assign the Statistics instance here
            donation_amount=Donation_amount,
            donation_category=donation_category,
            donation_description=donation_description
        )
        donation_obj.save()
        Profile.objects.filter(user_id=UserName).update(KarmaPoints=Profile.objects.get(user_id=UserName).KarmaPoints+Donation_amount)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'leaderboard_group',
            {
                'type': 'send_leaderboard',
            }
        )
    context = {
        "user_id": request.user
    }
    return render(request, "./Donation.html", context)

def donate_main(request):
    qs = Statistics.objects.all().order_by('value')
    qs.reverse()
    if request.method == 'POST':
        Donaters_UserID = request.POST.get('Donaters_UserID')
        response =Statistics.objects.get(Donaters_UserID=Donaters_UserID)
        if response:
            New_Value = response.value
        Statistics.objects.get_or_create(Donaters_UserID=Donaters_UserID,value=New_Value)
        
      
        print(Donaters_UserID)
        
        return redirect ("Donation_STATS:Donaters_Dashboard",slug=response.slug)
    return render(request,".\main.html",{"qs":qs})



def Donaters_Dashboard(request,slug):
    print(slug)
    obj = get_object_or_404(Statistics,slug=slug)
    print(obj)
    Donations = Donation.objects.filter(user_name=obj)
    
    
    
    return render(request,f".\Donaters_DashBoard.html",{
        "name": obj.Donaters_UserID,
        "value": obj.value,
        "slug": obj.slug,
        "user":request.user.username,
        "Donations":Donations
})