from django.shortcuts import render,redirect,get_object_or_404
from .models import Donation,Statistics
from login.models import Transactions,KarmaPoints,Profile

# Create your views here.

from django.shortcuts import render
from .models import Statistics, Donation

def donaters(request):
    user_id = request.user
    if request.method == "POST":
        
        user_id= request.user
        Name= user_id.username
        auth_0_user = user_id.social_auth.get(provider='auth0')
        AuthO_user_id= auth_0_user.uid
        print(AuthO_user_id)
        
        try:
            Donation_amount = int(request.POST.get("Donation_amount"))
            
            
        except (ValueError, TypeError):
            # Handle the case where Donation_amount is not a valid integer
            return render(request, "./Donation.html", {"error": "Invalid donation amount"})

        Donaters_UserID = request.POST.get("Donaters_UserID")

        if not Donaters_UserID:
            # Handle the case where Donaters_UserID is not provided
            return render(request, "./Donation.html", {"error": "User ID is required"})
        print("error point 1")
        obj, created = Statistics.objects.get_or_create(Donaters_UserID=Name, defaults={'value': 0, 'ranking': 0})
        if created:
            obj.value = Donation_amount
        else:
            obj.value += Donation_amount

        obj.save()
        print("error poiunt 2")
        # Create a new Donation record
       # create code for transaction
        payer_id = user_id
        payee_id = "admin"
        transaction_type = "Donation"
        transaction_amount = Donation_amount
        transaction_obj = Transactions.objects.create(
            payer_id=payer_id,
            payee_id=payee_id,
            transaction_type=transaction_type,
            transaction_amount=transaction_amount
        )
        # create code for karma points
        karma_points_obj, karma_points_created = KarmaPoints.objects.get_or_create(
            user_id=payer_id,
            karma_points_type="Donation",
            karma_points=(Donation_amount/100),
            reference_id=transaction_obj.transaction_id
        )
        
        
        # create code for Donation
        donation_obj = Donation.objects.create(
            Donaters_UserID=Donaters_UserID,
            user_name=user_id,
            donation_amount=Donation_amount,
            donation_category="Donation",
            donation_description="Donation"
        )
    context={
        "user_id":request.user
    }
    return render(request, "./Donation.html", context)

def donate_main(request):
    qs = Statistics.objects.all().order_by('ranking')
    if request.method == 'POST':
        Donaters_UserID = request.POST.get('Donaters_UserID')
        response =Statistics.objects.get(Donaters_UserID=Donaters_UserID)
        if response:
            New_Value = response.value
        Statistics.objects.get_or_create(Donaters_UserID=Donaters_UserID,value=New_Value)
        
      
        print(Donaters_UserID)
        
        return redirect ("Donation_STATS:Donaters_Dashboard",slug=response.slug)
    return render(request,".\main.html",{"qs":qs})#,{"qs":qs}



def Donaters_Dashboard(request,slug):
    print(slug)
    obj = get_object_or_404(Statistics,slug=slug)
    print(obj)
    
    return render(request,'./Donaters_DashBoard.html',{
        "name": obj.Donaters_UserID,
        "value": obj.value,
        "slug": obj.slug,
        "user":request.user
    })