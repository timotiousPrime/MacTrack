from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from members.forms import Login_Form

# Create your views here.
@login_required
def landingPage(request):
    context = {'greeting': "Welcome to the landing page!"}
    return render(request, 'main/startPage.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'error': "Username and/or password is incorrect",
                "form": Login_Form
            }
            return render (request, 'main/loginPage.html', context)
        else:
            login(request, user)
            print ("User has been authenticated!")
            print (user)
            return redirect('User_Profile', user)
    else:
        context = {
            'form': Login_Form
        }
        return render(request, 'main/loginPage.html', context)