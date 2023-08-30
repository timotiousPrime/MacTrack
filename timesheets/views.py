from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import TaskTime
from timesheets.forms import Task_Timer_Form
from django.utils import timezone


# Create your views here.
def task_timer(request):
    today = timezone.localdate()
    user = get_object_or_404(User, username=request.user.username)
    user_tasks = TaskTime.objects.filter(user=request.user.id)
    todays_tasks = user_tasks.filter(date_created__date=today)

    """
    Check for ongoing tasks from previous days, and create new tasks for today if any ongoing
    """
    # Get ongoing tasks from user
    users_ongoing_tasks = user_tasks.filter(is_ongoing=True)
    # ogt = (job_code, ancillary_code, description)

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
            newTask = TaskTime(user=request.user, ancillary_code=og[1], description=og[2], job_code=og[0], is_ongoing=True)
            newTask.save()

    # Get updated tasks
    user_tasks = TaskTime.objects.filter(user=request.user.id)
    todays_tasks = user_tasks.filter(date_created__date=today)

    context = {
        "user": user,
        "taskTimerForm": Task_Timer_Form,
        "userTasks": user_tasks,
        "todays_tasks": todays_tasks,
    }

    return render(request, "timesheets/taskTimerPage.html", context)


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
        return HttpResponse(task.elapsed_time)

    return redirect("Task_Timer")


def edit_timer(request, task_id):
    """View is called when a task timers' (tte) edit button has been clicked or when a tte form is submitted"""
    task = TaskTime.objects.get(id=task_id)
    if request.method == "POST":
        form = Task_Timer_Form(request.POST or None, instance=task)
        if form.is_valid():
            task.date_edited = timezone.now()
            task.save()
            return render(request, "partials/taskTableRow.html", {"task": task})

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
