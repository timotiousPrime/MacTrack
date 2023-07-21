from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from .models import TaskTime
from timesheets.forms import Task_Timer_Form

# Create your views here.
def task_timer(request):
    user = get_object_or_404(User, username=request.user.username)
    # user_task_times = get_list_or_404(TaskTime, user=request.user.id)


    context = {
        'user': user,
        'taskTimerForm': Task_Timer_Form,
        # 'userTaskTimes': user_task_times,
    }
    return render(request, 'timesheets/taskTimer.html', context)


def create_task(request):
    user = request.user
    context = {
        "user": user,

    }
    return render(request, "timesheets/taskTimer.html", context)


def start_timer(request):
    context = {

    }
    return render(request, "timesheets/taskTimer.html", context)