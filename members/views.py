from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from members.forms import Login_Form

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

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user
    }
    return render(request, 'members/userProfile.html', context)