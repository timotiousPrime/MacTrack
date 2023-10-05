# Import Models
from .models import TaskTime
from django.contrib.auth.models import User
# Time Imports
from datetime import timedelta
from django.utils import timezone
# Forms
from timesheets.forms import Task_Timer_Form


def get_hrs_mins(total_time):
    hours, remainder = divmod(total_time.seconds, 3600)
    minutes = remainder // 60
    return (hours, minutes)


def calculate_total_time(tasks):
    # Initialize total duration
    total_duration = timedelta()

    # Calculate total duration by iterating through tasks
    for task in tasks:
        total_duration += task.elapsed_time

    # Calculate total hours and minutes
    total_hours, total_minutes = get_hrs_mins(total_duration)

    return total_hours, total_minutes


# ***** WIP *****
# def delete_old_timeless_tasks(user_id):
#     today = timezone.localdate()
#     print("Today is: ", today)
#     old_user_tasks = TaskTime.objects.filter(user=user_id).filter(elapsed_time=None).exclude(date_created__date=today)
#     for task in old_user_tasks:
#         print("deleting: ", task)
#         # task.delete()


def stop_running_tasks(userId):
    running_tasks = TaskTime.objects.filter(user=userId, is_running=True)
    for rt in running_tasks:
        rt.is_running = False
        rt.time_stopped = timezone.now()
        rt.get_elapsed_time()
        rt.date_edited = timezone.now()
        rt.save()


def update_ongoing_tasks(userId):
    today = timezone.localdate()

    user = User.objects.get(id=userId)

    # Get TaskTime Lists
    ongoing_tasks = TaskTime.objects.filter(user=userId, is_ongoing=True).exclude(date_created=today)
    todays_tasks = TaskTime.objects.filter(user=userId, date_created__date=today)
    
    # Create a set of on going tasks with no duplicates of job code, ancillary code and description
    og_tasks = {(t.job_code, t.ancillary_code, t.description) for t in ongoing_tasks}
    
    # Check if any of the ongoing tasks are in todays tasks already, if not create new ongoing tasks for today
    for og in og_tasks:
        task_exists = False
        for tt in todays_tasks:
            if og[0] == tt.job_code and og[1] == tt.ancillary_code and og[2] == tt.description:
                task_exists = True
        if not task_exists:
            newTask = TaskTime(user=user, ancillary_code=og[1], description=og[2], job_code=og[0], is_ongoing=True, is_running=False, elapsed_time=timedelta(0))
            newTask.save()

    print ("Ongoing Tasks: ", og_tasks)


def get_users_task_stats_today(users_tasks_today):
    # Total time
    todays_total_hrs, todays_total_minutes = calculate_total_time(users_tasks_today)
    
    # Longest Task
    longest_task = None
    for task in users_tasks_today:
        if longest_task is None or task.elapsed_time > longest_task.elapsed_time:
            longest_task = task

    # Design time
    design_tasks = users_tasks_today.filter(description="Des")
    design_hrs, design_mins = calculate_total_time(design_tasks)

    # Tasks Count
    todays_task_count = len(users_tasks_today.exclude(ancillary_code="Break"))
    print("Total Tasks Today: ", todays_task_count)

    # Get Tasks info
    tasks_info = {}
    for task in users_tasks_today:
        tasks_info[task.id] = {"is_running": task.is_running,
                             "time_started": task.time_started
                             }
    
    todays_stats= {
        "total_hrs": todays_total_hrs,
        "total_mins": todays_total_minutes,
        "longest_task": longest_task,
        "design_hrs": design_hrs,
        "design_mins": design_mins,
        "task_count": todays_task_count,
        "tasks_info": tasks_info,
    }
    print("Total Tasks Stats: ", todays_stats)
    return todays_stats


def get_task_timer_context(userId):
    # Todays Date
    today = timezone.localdate()

    # Get all tasks for the user that were created today
    todays_tasks = TaskTime.objects.filter(user=userId, date_created__date=today)
    
    # Get user stats from tasks for the day
    todays_stats = get_users_task_stats_today(todays_tasks)

    # Context
    context = {
        "title": "Task Timer",
        "task_timer_form": Task_Timer_Form,
        "todays_tasks": todays_tasks,
        "todays_stats": todays_stats,
    }
    return context