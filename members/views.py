from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from members.forms import Login_Form, User_Profile_Form
from django.contrib.auth.models import User
from members.models import User_Profile

# Create your views here.

# LoginView
def loginView(request):
    if request.method == "GET":
        context = {
            'form': Login_Form()
        }
        return render(request, 'members/loginPage.html', context)
    
    if request.method == "POST":
        print('method is post')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            print('user is none')
            context = {
                'error': "Username and/or password is incorrect",
                "form": Login_Form
            }
            return render(request, 'members/loginPage.html', context)
        else:
            login(request, user)
            print('login successful')
            return redirect('Home')


# LogoutView
def logoutView(request):
    logout(request)
    return redirect('Home')


def userProfileView(request):
    # userProfileView
    if request.method == 'GET':
        try:
            profile = request.user.user_profile
        except User_Profile.DoesNotExist:
            context = {
                'errror': "There was an error retrieving this user's profile. Please contect your administrator.",
            }
            return redirect('Home')
    
        context = {
            'profile': profile
        }
        return render(request, 'members/userProfile.html', context)

    # updateUserProfileView
    if request.method == 'POST':
        user = request.user
        form = User_Profile_Form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('getUserProfile')

    context = {}
    return render(request, 'members/updateUserProfile.html', context)


