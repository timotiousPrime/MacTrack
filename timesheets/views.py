from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import TaskTime
from timesheets.forms import Task_Timer_Form
from django.utils import timezone


# Create your views here.
def task_timer(request):
    user = get_object_or_404(User, username=request.user.username)
    user_tasks = list(TaskTime.objects.filter(user=request.user.id))

    context = {
        "user": user,
        "taskTimerForm": Task_Timer_Form,
        "userTasks": user_tasks,
    }

    return render(request, "timesheets/taskTimer.html", context)


def create_task(request):
    if request.method == "POST":
        form = Task_Timer_Form(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.time_started = timezone.now()
            task.is_running = True
            task.save()
            return redirect("Task_Timer")

    return redirect("Task_Timer") 


def start_timer(request, task_id):
    if request.method == "POST":
        task = TaskTime.objects.get(id=task_id)
        task.is_running = True
        task.time_started = timezone.now()
        task.date_edited = timezone.now()
        task.save()
        return HttpResponse(status=200)
    
    return redirect("Task_Timer")


def stop_timer(request, task_id):
    if request.method == "POST":
        task = TaskTime.objects.get(id=task_id)
        task.is_running = False
        task.time_stopped = timezone.now()
        task.get_elapsed_time()
        task.date_edited = timezone.now()
        task.save()
        return HttpResponse(status=200)
    
    return redirect("Task_Timer")


def edit_timer(request, task_id):
    print("EDIT VIEW CALLED**************")
    task = TaskTime.objects.get(id=task_id)
    if request.method == "POST":
        print("******** REQUEST.POST")
        form = Task_Timer_Form(request.POST or None, instance=task)
        if form.is_valid():
            task.date_edited = timezone.now()
            task.save() 
            return redirect("Task_Timer")
    
    if request.method == "GET":
        print("********Getting Edit view********")
        form = Task_Timer_Form(instance=task)
        context = {
            "form": form,
            "task": task,
        }
        return render(request, "timesheets/edit.html", context)

    return redirect("Task_Timer")


def delete_timer(request, task_id):
    if request.method == "POST":    
        task = TaskTime.objects.get(id=task_id)
        task.delete()
        return HttpResponse(status=200)
    
    return redirect("Task_Timer")
