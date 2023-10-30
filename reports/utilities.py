from django.contrib.auth.models import User
from timesheets.models import TaskTime
from members.models import User_Profile



# Utility functions for report views

def adminReportsContext():
    
    tasks = TaskTime.objects.all().exclude(elapsed_time = None).order_by("-date_created", "user", "job_code", "ancillary_code", "description")[:5]

    return {
        "title": "Admin Reports",
        "tasks": tasks
    }