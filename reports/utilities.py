from django.shortcuts import render
from datetime import timedelta

# Models 
from django.contrib.auth.models import User
from timesheets.models import TaskTime
from members.models import User_Profile

# Import graph components
from .templates.graphs.barChart import get_graph_components

# Utility functions for report views

def adminReportsContext():
    
    tasks = TaskTime.objects.all().exclude(elapsed_time = timedelta(seconds=0)).order_by("-date_created", "user", "job_code", "ancillary_code", "description")[:5]

    return {
        "title": "Admin Reports",
        "tasks": tasks
    }

def designerReportContext():
    # Get all task times 
    task_times = list(TaskTime.objects.all())

    # Add up all the time for each job code
    job_code_hours = {}

    for t in task_times:
        if t.job_code not in job_code_hours:
            job_code_hours[str(t.job_code)] = t.elapsed_time
        else:
            job_code_hours[str(t.job_code)] += t.elapsed_time

    # We need lists for the input for the x and y axis's respectively
    jc_list = list(job_code_hours.keys())
    et_list = list(job_code_hours.values())

    # We want the time in hours
    if et_list is not None:
        et_list = [t.total_seconds() / 3600 for t in et_list]
    else:
        et_list = []


    script, div = get_graph_components(jc_list, et_list)

    context = {
        "title": "Task Timer Reports",
        "reports": "Here are some task timer reports",
        "script": script,
        "div": div
    }

    return context
