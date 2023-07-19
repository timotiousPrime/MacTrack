from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from .models import TaskTime

# Create your views here.
def task_timer(request):
    
    user = get_object_or_404(User, username=request.user.username)
    # user_task_times = get_list_or_404(TaskTime, user=request.user.id)

    context = {
        'user': user,
        # 'userTaskTimes': user_task_times,
    }
    return render(request, 'timesheets/taskTimer.html', context)