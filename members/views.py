from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from members.forms import Login_Form
from timesheets.models import TaskTime
from .templates.graphs.barChart import get_graph_components

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

def user_profile(request, username):
    # Get all task times 
    user_task_times = TaskTime.objects.filter(user=request.user.id).exclude(elapsed_time=None)

    # Add up all the time for each job code
    job_code_hours = {}

    for t in user_task_times:
        if t.job_code not in job_code_hours:
            job_code_hours[t.job_code] = (t.elapsed_time.seconds / 3600)
        else:
            job_code_hours[t.job_code] += (t.elapsed_time.seconds  / 3600)

    # We need lists for the input for the x and y axis's respectively
    jc_list = [project.job_code for project in job_code_hours.keys()]
    print("Job Codes: ", jc_list)
    et_list = list(job_code_hours.values())
    print("Elapsed Times: ",et_list)
    
    script, div = get_graph_components(jc_list, et_list)

    # Get user Task times for history 
    user = get_object_or_404(User, username=username)
    # user_tasks = get_list_or_404(TaskTime, user)
    user_tasks = list(TaskTime.objects.filter(user=user).exclude(elapsed_time=None).order_by('-id'))[:5]

    context = {
        "title": "Dashboard",
        'user': user,
        'user_tasks': user_tasks,
        "reports": "Here are some task timer reports",
        "script": script,
        "div": div
    }
    return render(request, 'members/userProfile.html', context)


def user_task_history(request, username):
    print(username)
    user_tasks = TaskTime.objects.filter(user=request.user.id).exclude(elapsed_time=None).order_by('-id')
    context = {
        "title": "Task History",
        "user_tasks": user_tasks
    }
    return render (request, "timesheets/taskTimeHistory.html", context)

