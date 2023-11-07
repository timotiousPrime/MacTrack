from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from members.forms import Login_Form
from timesheets.models import TaskTime
from .templates.graphs.barChart import get_graph_components

def getAdminDashboardContext():
    # Get all task times 
    user_task_times = TaskTime.objects.exclude(elapsed_time=None)

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
    # user = get_object_or_404(User, username=username)
    # user_tasks = get_list_or_404(TaskTime, user)
    # user_tasks = list(TaskTime.objects.filter(user=user).exclude(elapsed_time=None).order_by('-id'))[:5]

    context = {
        "title": "Dashboard",
        # 'user': user,
        # 'user_tasks': user_tasks,
        "reports": "Here are some task timer reports",
        "script": script,
        "div": div,
    }

    return context


def getDesignerDashboardContext(userId):

    user = User.objects.get(id=userId)

    # Get all task times 
    user_task_times = TaskTime.objects.filter(user=userId).exclude(elapsed_time=None)

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

    return context


def getManagerDashboardContext(userId):

    user = User.objects.get(id=userId)

    # Get all task times 
    user_task_times = TaskTime.objects.filter(user=userId).exclude(elapsed_time=None)

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

    return context


def getFitterDashboardContext(userId):

    user = User.objects.get(id=userId)

    # Get all task times 
    user_task_times = TaskTime.objects.filter(user=userId).exclude(elapsed_time=None)

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

    return context


def getMachinistDashboardContext(userId):

    user = User.objects.get(id=userId)

    # Get all task times 
    user_task_times = TaskTime.objects.filter(user=userId).exclude(elapsed_time=None)

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

    return context


def getElectricianDashboardContext(userId):

    user = User.objects.get(id=userId)

    # Get all task times 
    user_task_times = TaskTime.objects.filter(user=userId).exclude(elapsed_time=None)

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

    return context


def getGeneralDashboardContext(userId):

    user = User.objects.get(id=userId)

    # Get all task times 
    user_task_times = TaskTime.objects.filter(user=userId).exclude(elapsed_time=None)

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

    return context


def getWelderDashboardContext(userId):

    user = User.objects.get(id=userId)

    # Get all task times 
    user_task_times = TaskTime.objects.filter(user=userId).exclude(elapsed_time=None)

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

    return context

