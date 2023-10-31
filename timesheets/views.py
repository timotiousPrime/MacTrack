# Django functions
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Models
from .models import TaskTime
from django.contrib.auth.models import User
# Forms
from timesheets.forms import Task_Timer_Form
# Time functions
from django.utils import timezone
# Utility Functions
from .utilities import get_task_timer_context, stop_running_tasks, update_ongoing_tasks


# Create your views here.
@login_required
def task_timer(request):
    userId = get_object_or_404(User, username=request.user.username).id

    # Update ongoing tasks
    update_ongoing_tasks(userId)

    # Context: title, task_timer_form, todays_tasks, todays_stats
    context = get_task_timer_context(userId)

    return render(request, "timesheets/taskTimerPage.html", context)


def create_task(request):
    if request.method == "POST":
        today = timezone.localdate()

        form = Task_Timer_Form(request.POST)
        if form.is_valid():
            stop_running_tasks(request.user.id)
            task = form.save(commit=False)
            task.user = request.user
            task.time_started = timezone.now()
            task.is_running = True
            task.save()

            # Context: title, task_timer_form, todays_tasks, todays_stats
            context = get_task_timer_context(request.user.id)
            render(request, "partials/usersTodaysTaskTable.html", context)

    return redirect("Task_Timer")


def update_ongoing(request, task_id):
    today = timezone.localdate()
    task = TaskTime.objects.get(id=task_id)
    sameTasks = TaskTime.objects.filter(job_code=task.job_code, ancillary_code=task.ancillary_code, description=task.description, user=request.user.id)
    todays_tasks = TaskTime.objects.filter(user=request.user.id, date_created__date=today)
    if request.method == "POST":
        if task.is_ongoing:
            for t in sameTasks:
                t.is_ongoing = False
                t.save()
        else:
            for t in sameTasks:
                t.is_ongoing = True
                t.save()
        context = {
            "todays_tasks": todays_tasks
        }
        print("stuff has been updated")
        return render(request, "partials/usersTodaysTaskTable.html", context)
    return HttpResponse(status=404)


def start_timer(request, task_id):
    userId = request.user.id
    # today = timezone.localdate()
    task = TaskTime.objects.get(id=task_id)
    # todays_tasks = TaskTime.objects.filter(user=userId, date_created__date=today).exclude(elapsed_time=None)
    if not task.is_running:
        if request.method == "POST":
            stop_running_tasks(userId)
            task.is_running = True
            task.time_started = timezone.now()
            task.date_edited = timezone.now()
            task.save()
            # running_task_info = {"id": task.id, "time_started":  task.time_started, "elapsed_time": task.elapsed_time.seconds}
            # Context: title, task_timer_form, todays_tasks, todays_stats
            context = get_task_timer_context(request.user.id)
            return render(request, "partials/usersTodaysTaskTable.html", context)

    return redirect("Task_Timer")


def stop_timer(request, task_id):
    task = TaskTime.objects.get(id=task_id)
    if task.is_running:
        if request.method == "POST":
            task.is_running = False
            task.time_stopped = timezone.now()
            task.get_elapsed_time()
            task.date_edited = timezone.now()
            task.save()
            context = {
                "task": task,
            }
            return render(request, "partials/pausedRow.html", context)

    return redirect("Task_Timer")


def edit_timer(request, task_id):
    """View is called when a task timers' edit (TTE) button has been clicked or when a TTE form is submitted"""
    task = TaskTime.objects.get(id=task_id)
    if request.method == "POST":
        form = Task_Timer_Form(request.POST or None, instance=task)
        if form.is_valid():
            task.date_edited = timezone.now()
            task.save()
            
            context = get_task_timer_context(request.user.id)
            return render(request, "partials/taskTimer.html", context)

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


def task_history_edit_timer(request, task_id):
    task = TaskTime.objects.get(id=task_id)
    if request.method == "POST":
        form = Task_Timer_Form(request.POST or None, instance=task)
        if form.is_valid():
            task.date_edited = timezone.now()
            task.save()
            
            context = get_task_timer_context(request.user.id)
            return render(request, "partials/taskTimer.html", context)

    if request.method == "GET":
        print("********Getting Edit view********")
        form = Task_Timer_Form(instance=task)
        context = {
            "form": form,
            "task": task,
        }
        return render(request, "timesheets/edit.html", context)
    template = ""
    context = {}
    return redirect("User_Task_History")