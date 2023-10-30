from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from members.forms import Login_Form
from timesheets.models import TaskTime
from .templates.graphs.barChart import get_graph_components
from members.models import User_Profile
from .utilities import getAdminDashboardContext, getDesignerDashboardContext

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
                    template = 'members/adminDashboard.html'
                case _:
                    print("Not valid user")
    
    return render(request, template, context)

@login_required
def user_task_history(request, username):
    print(username)
    user_tasks = TaskTime.objects.filter(user=request.user.id).exclude(elapsed_time=None).order_by('-id')
    context = {
        "title": "Task History",
        "user_tasks": user_tasks
    }
    return render (request, "timesheets/taskTimeHistory.html", context)

