from django.shortcuts import render
from login.models import Profile
from http.client import HTTPResponse
# Create your views here.
def admin(request):
    return render(request, f'./admin.html')
    # user_name=request.user.username
    # User_Type=Profile.objects.get(user_id=user_name).user_type
    # if User_Type=="Admin":
    #     return render(request, 'admin.html')
    # else:
    #     return render(request, 'admin.html')
    #     # return HTTPResponse("You are not authorized to view this page")
    
    