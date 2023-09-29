# Import Models
from .models import TaskTime
# Time Imports
from datetime import timedelta
from django.utils import timezone
# Forms
from timesheets.forms import Task_Timer_Form


def calculate_total_time(tasks):
    # Initialize total duration
    total_duration = timedelta()

    # Calculate total duration by iterating through tasks
    for task in tasks:
        total_duration += task.elapsed_time

    # Calculate total hours and minutes
    total_hours, remainder = divmod(total_duration.seconds, 3600)
    total_minutes = remainder // 60

    return total_hours, total_minutes



def delete_old_timeless_tasks(user_id):
    today = timezone.localdate()
    print("Today is: ", today)
    old_user_tasks = TaskTime.objects.filter(user=user_id).filter(elapsed_time=None).exclude(date_created__date=today)
    for task in old_user_tasks:
        print("deleting: ", task)
        # task.delete()



def stop_running_tasks(userId):
    running_tasks = TaskTime.objects.filter(user=userId).filter(is_running=True)
    for rt in running_tasks:
        rt.is_running = False
        rt.time_stopped = timezone.now()
        rt.get_elapsed_time()
        rt.date_edited = timezone.now()
        rt.save()


def get_task_timer_context(user){
    todays_stats = {}
    todays_tasks = null

    # Context
    context = {
        "title" : "Task Timer",
        "user" : user,
        "task_timer_form" : Task_Timer_Form,
        "todays_tasks" : todays_tasks,
        "todays_stats" : todays_stats,
        "running_task" : running_task_info,
    }
}