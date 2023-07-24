from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from .models import TaskTime
from timesheets.forms import Task_Timer_Form
from django.utils import timezone


# Create your views here.
def task_timer(request):
    user = get_object_or_404(User, username=request.user.username)
    # user_task_times = get_list_or_404(TaskTime, user=request.user.id)
    user_tasks = list(TaskTime.objects.filter(user=request.user.id))

    context = {
        "user": user,
        "taskTimerForm": Task_Timer_Form,
        "userTasks": user_tasks,
    }

    return render(request, "timesheets/taskTimer.html", context)


def create_task(request):
    user = get_object_or_404(User, username=request.user.username)
    if request.method == "POST":
        form = Task_Timer_Form(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.time_started = timezone.now()
            task.is_running = True
            task.save()

            return redirect("Task_Timer")

    context = {
        "user": user,
        "taskTimerForm": Task_Timer_Form,
    }
    return render(request, "timesheets/taskTimer.html", context)


def start_timer(request, task_id):
    if request.method == "POST":
        task = TaskTime.objects.get(id=task_id)
        task.is_running = True
        task.time_started = timezone.now()
        task.date_edited = timezone.now()
        task.save()
        return redirect("Task_Timer")
    
    user = request.user
    userTasks = TaskTime.objects.filter(user=user)
    context = {
        "taskTimerForm": Task_Timer_Form,
        "user": user,
        "userTasks": userTasks
    }
    return render(request, "timesheets/taskTimer.html", context)


def stop_timer(request, task_id):
    if request.method == "POST":
        task = TaskTime.objects.get(id=task_id)
        task.is_running = False
        task.time_stopped = timezone.now()
        task.get_elapsed_time()
        task.date_edited = timezone.now()
        task.save()
        return redirect("Task_Timer")
    
    user = request.user
    userTasks = TaskTime.objects.filter(user=user)
    context = {
        "taskTimerForm": Task_Timer_Form,
        "user": user,
        "userTasks": userTasks
    }
    return render(request, "timesheets/taskTimer.html", context)


def edit_timer(request, task_id):
    if request.method == "POST":
        task = TaskTime.objects.get(id=task_id)
        return redirect("Task_Timer")

    user = request.user
    userTasks = TaskTime.objects.filter(user=user)
    context = {
        "taskTimerForm": Task_Timer_Form,
        "user": user,
        "userTasks": userTasks
    }
    return render(request, "timesheets/taskTimer.html", context)


def delete_timer(request, task_id):
    print("*****DELETE BUTTON CLICKED*****")
    if request.method == "POST":    
        task = TaskTime.objects.get(id=task_id)
        task.delete()
        return redirect("Task_Timer")

    user = request.user
    userTasks = TaskTime.objects.filter(user=user)
    context = {
        "taskTimerForm": Task_Timer_Form,
        "user": user,
        "userTasks": userTasks
    }
    return render(request, "timesheets/taskTimer.html", context)