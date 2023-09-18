from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from members.forms import Login_Form
from timesheets.models import TaskTime
from .templates.graphs.barChart import get_graph_components
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum, Count



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

    # Get all task times 
    user_task_times = TaskTime.objects.filter(user=request.user.id).exclude(elapsed_time=None)

    # Add up all the time for each job code
    job_code_hours = {}

    # for t in user_task_times:
    #     job_code = str(t.job_code)
    #     if t.elapsed_time is None:
    #         elapsed_time = datetime.timedelta(seconds=0)
    #     else:
    #         elapsed_time = t.elapsed_time
    #     # elapsed_time = str(t.elapsed_time) if t.elapsed_time is not None else datetime.timedelta(seconds=0)
    #     print(elapsed_time)
    #     if t.job_code not in job_code_hours:
    #         job_code_hours[job_code] = elapsed_time.seconds
    #     else:
    #         job_code_hours[job_code] += elapsed_time.seconds

    for t in user_task_times:
        if t.job_code not in job_code_hours:
            job_code_hours[t.job_code] = (t.elapsed_time.seconds / 3600)
        else:
            job_code_hours[t.job_code] += (t.elapsed_time.seconds  / 3600)
    
    print("Job Code Hours: ", job_code_hours)

    # # We need lists for the input for the x and y axis's respectively
    # jc_list = list(job_code_hours.keys())
    # print("Job Codes: ", jc_list)
    # et_list = list(job_code_hours.values())
    # print("Elapsed Times: ",et_list)

    jc_list, et_list = list(job_code_hours.keys()), list(job_code_hours.values())

    print(jc_list, et_list)

    # We want the time in hours
    # if et_list is not None:
    #     et_list = [t.total_seconds() / 3600 for t in et_list if t is not None and hasattr(t, 'total_seconds')]
    # else:
    #     et_list = []

    script, div = get_graph_components(jc_list, et_list)

    # Get user Task times for history 
    user = get_object_or_404(User, username=username)
    # user_tasks = get_list_or_404(TaskTime, user)
    user_tasks = list(TaskTime.objects.filter(user=user).exclude(elapsed_time=None).order_by('-id'))[:5]

    context = {
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
        "user_tasks": user_tasks
    }
    return render (request, "timesheets/taskTimeHistory.html", context)

