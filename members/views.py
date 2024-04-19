from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from members.forms import Login_Form
from timesheets.models import TaskTime
from .templates.graphs.barChart import get_graph_components
from members.models import User_Profile
from .utilities import getAdminDashboardContext, getDesignerDashboardContext, getManagerDashboardContext, getFitterDashboardContext, getMachinistDashboardContext, getElectricianDashboardContext, getWelderDashboardContext, getGeneralDashboardContext
from django.http import HttpResponse

from django.contrib.auth.hashers import make_password
# Generic Class Views
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
)

# Forms 
from .forms import New_User_Form, User_Profile_Form, Edit_User_Profile_Form

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
            return redirect('User_Profile')
    else:
        context = {
            'form': Login_Form
        }
        return render(request, 'members/loginPage.html', context)
    

def logout_view(request):
    logout(request)
    return redirect('Home')

@login_required
def user_profile(request, username):
    userId = User.objects.get(username=username)
    up = User_Profile.objects.get(user_id = userId)
    match up.role:
                case "Des":
                    print("Des logging in!")
                    context = getDesignerDashboardContext(userId.id)
                    template = 'members/userProfile.html'
                case "Adm":
                    print("Adm logging in!")
                    context = getAdminDashboardContext()
                    template = 'members/managerDashboard.html'
                case "Man":
                    print("Manager logging in!")
                    context = getManagerDashboardContext(userId.id)
                    template = 'members/managerDashboard.html'
                case "Fit":
                    print("Fitter logging in!")
                    context = getFitterDashboardContext(userId.id)
                    template = 'members/userProfile.html'
                case "Mac":
                    print("Machinist logging in!")
                    context = getMachinistDashboardContext(userId.id)
                    template = 'members/machinistProfile.html'
                case "Ele":
                    print("Electrician logging in!")
                    context = getElectricianDashboardContext(userId.id)
                    template = 'members/electricianProfile.html'
                case "Wel":
                    print("Welder logging in!")
                    context = getWelderDashboardContext(userId.id)
                    template = 'members/welderProfile.html'
                case _:
                    print("General user type logging in!", up.role)
                    context = getGeneralDashboardContext(userId.id)
                    template = 'members/userProfile.html'
    
    return render(request, template, context)


@login_required
def user_task_history(request, username):
    print(username)
    user_tasks = TaskTime.objects.filter(user=request.user.id).order_by('-id')
    context = {
        "title": "Task History",
        "user_tasks": user_tasks
    }
    return render (request, "timesheets/taskTimeHistory.html", context)

class UserListView(ListView):
    template_name = "members/userList.html"
    model = User_Profile
    paginate_by = 14

    def get_context_data(self, **kwargs):
        context = super(UserListView,self).get_context_data(**kwargs)
        context["title"] = "User List"
        
        return context
    

class CreateNewUser(CreateView):
    template_name = "members/createUser.html"
    model = User


def addNewUser(request):
    context = {
        "title": "Add New User",
        "user_form": New_User_Form(prefix="user_form"),
        "user_profile": User_Profile_Form(prefix="user_profile")
    }
    template = "members/newUserFormBody.html"

    if request.method == "POST":
        newUserForm = New_User_Form(request.POST, prefix="user_form")
        userProfileForm = User_Profile_Form(request.POST, prefix="user_profile")


        if newUserForm.is_valid():
            print("User Form is Valid!")
            newUser = newUserForm.save(commit=False)
            newUser.password = make_password(newUserForm.cleaned_data['password'])
            newUser.save()
            
            profile = User_Profile.objects.get(user=newUser)
            profile_form = User_Profile_Form(request.POST, prefix="user_profile", instance=profile)
            
            if profile_form.is_valid():
                print("Profile form is valid!")
                profile_form.save()
                return HttpResponse(status=201)
            else:
                print("Profile Form is not valid:")
                return HttpResponse(status=501)

            # Valid Form POST response
        
        context['user_form'] = New_User_Form(request.POST, prefix="user_form")
        context['user_profile'] = User_Profile_Form(request.POST, prefix="user_profile")
        # Non valid form POST response
        return render(request, template, context)
    

    # GET request response
    return render(request, template, context)

def editUser(request, userId):
    user = User.objects.get(id=userId)
    profile = User_Profile.objects.get(user=userId)
    newUserForm = New_User_Form(instance=user, prefix="user_form")
    profile_form = Edit_User_Profile_Form(instance=user.user_profile, prefix="user_profile")
    template = "members/editUserFormBody.html"
    context = {
        "user": user,
        "title": "Edit User",
        "user_form": newUserForm,
        "user_profile": profile_form,
    }
    if request.method == "POST":
        print("Updating User Details")
        userForm=New_User_Form(request.POST, prefix="user_form", instance=user)
        profileForm=User_Profile_Form(request.POST, prefix="user_profile", instance=profile)
        if userForm.is_valid() and profileForm.is_valid():
            print("Both forms are valid!")
            profile.save()
            if userForm.cleaned_data['password']:
                print("Updating user Password")
                user.password = make_password(userForm.cleaned_data['password'])

            user.save()
            return HttpResponse(status="201")
            # return redirect("User_List")
        else:
            print("Forms not valid")
            return HttpResponse(status=501)

        context['user_form'] = New_User_Form(request.POST, instance=user, prefix="user_form")
        context['user_profile'] = Edit_User_Profile_Form(request.POST, instance=profile, prefix="user_profile")

    print("Getting User edit Form")
    return render(request, template, context)