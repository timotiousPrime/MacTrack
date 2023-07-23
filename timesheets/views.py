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

    if len(user_tasks) > 1:
        print("its bigger than 1")

    if len(user_tasks) < 1:
        print("its SMALLER than 1")

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


def start_timer(request):
    context = {}
    return render(request, "timesheets/taskTimer.html", context)
