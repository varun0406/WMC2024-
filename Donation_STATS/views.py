from django.shortcuts import render,redirect,get_object_or_404
from .models import Donation,Statistics

# Create your views here.

def donate_main(request):
    qs= Statistics.objects.all()
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