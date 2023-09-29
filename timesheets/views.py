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
from datetime import timedelta
# Utility Functions
from .utilities import calculate_total_time, stop_running_tasks


# Create your views here.
@login_required
def task_timer(request):
    today = timezone.localdate()
    user = get_object_or_404(User, username=request.user.username)
    user_tasks = TaskTime.objects.filter(user=request.user.id)
    todays_tasks = user_tasks.filter(date_created__date=today)

    """
    Check for ongoing tasks from previous days, and create new tasks for today if any ongoing
    """
    # Get ongoing tasks from user
    users_ongoing_tasks = user_tasks.filter(is_ongoing=True).exclude(date_created=today)

    # Create a set of ongoing tasks - no duplicate tasks with the same jobcodes, ancillarycodes and descriptions
    og_tasks = set()
    for t in users_ongoing_tasks:
        og = (t.job_code, t.ancillary_code, t.description)
        og_tasks.add(og)
    
    # Check if any of the ongoing tasks are in todays tasks already, if not create new ongoing tasks for today
    for og in og_tasks:
        task_exists = False
        for tt in todays_tasks:
            if og[0] == tt.job_code and og[1] == tt.ancillary_code and og[2] == tt.description:
                task_exists = True
        if not task_exists:
            newTask = TaskTime(user=request.user, ancillary_code=og[1], description=og[2], job_code=og[0], is_ongoing=True, is_running=False, elapsed_time=timedelta(0))
            newTask.save()


    todays_tasks = todays_tasks.exclude(elapsed_time=None)
    # Calculate the total time
    todays_total_hrs, todays_total_minutes = calculate_total_time(todays_tasks)

    # Get Longest Task
    longest_task = None
    # Get total Design Time
    total_design_time = timedelta()

    for task in todays_tasks:
        if longest_task is None or task.elapsed_time > longest_task.elapsed_time:
            longest_task = task
        if task.description == "Des":
            total_design_time += task.elapsed_time

    # Calculate total hours and minutes
    total_design_hours, remainder = divmod(total_design_time.seconds, 3600)
    total_design_minutes = remainder // 60

    # Get todays task count, exclude breaks
    todays_task_count = todays_tasks.exclude(ancillary_code="Break")

    # Get Running Task
    try:
        running_task = user_tasks.get(is_running=True)
    except TaskTime.DoesNotExist:
        # Handle the case where there is no running task
        running_task = None  # You can set it to None or any other default value

    print("Running Task: ", running_task)

    if running_task == None:
        running_task_info = None
    else:
        running_task_info = {"id": running_task.id, "time_started": running_task.time_started, "elapsed_time": running_task.elapsed_time.seconds}

    context = {
        "title": "Task Timer",
        "user": user,
        "taskTimerForm": Task_Timer_Form,
        "userTasks": user_tasks,
        "todays_tasks": todays_tasks,
        "todays_total_hrs" : todays_total_hrs,
        "todays_total_minutes" : todays_total_minutes,
        "longest_task" : longest_task,
        "total_design_hours" : total_design_hours,
        "total_design_minutes" : total_design_minutes,
        "todays_task_count": todays_task_count,
        "running_task": running_task_info,
    }

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

            todays_tasks = TaskTime.objects.filter(user=request.user.id, date_created__date=today)
            running_task_info = {"id": task.id, "time_started": task.time_started, "elapsed_time": task.elapsed_time.seconds}
            context = {
                "todays_tasks": todays_tasks,
                "running_task": running_task_info
            }
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
    today = timezone.localdate()
    task = TaskTime.objects.get(id=task_id)
    todays_tasks = TaskTime.objects.filter(user=userId, date_created__date=today).exclude(elapsed_time=None)
    if not task.is_running:
        if request.method == "POST":
            stop_running_tasks(userId)
            task.is_running = True
            task.time_started = timezone.now()
            task.date_edited = timezone.now()
            task.save()
            running_task_info = {"id": task.id, "time_started":  task.time_started, "elapsed_time": task.elapsed_time.seconds}
            context = {
                "task": task,
                "todays_tasks": todays_tasks,
                "running_task": running_task_info,
            }
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
            context = {
                "task": task
            }
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
