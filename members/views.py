from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from members.forms import Login_Form, User_Profile

from members.models import User_Profile

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'error': "Username and/or password is incorrect",
                "form": Login_Form
            }
            return render (request, 'members/loginPage.html', context)
        else:
            login(request, user)
            print ("User has been authenticated!")
            print (user)
            return redirect('Home')
    else:
        context = {
            'form': Login_Form
        }
        return render(request, 'members/loginPage.html', context)
    

def logout_view(request):
    logout(request)
    return redirect('Home')


def userProfile(request, username):

    profiles = User_Profile.objects.all()
    print("*********************************************************")
    # print (profiles)
    context = {
        # "user": User_Profile.objects.get(username=username),
        "user": "User-TEST",
        "userProfileForm": User_Profile
    }
    return render (request, "members/userProfile.html", context)