from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from timesheets.models import TaskTime
from .templates.graphs.barChart import get_graph_components


# Create your views here.

def reports_landing_page(request):
    context = {
        "reports": "Here are some reports"
    }
    return render(request, "reports/landingPage.html", context)

# This is WORK IN PROGRESS
# def all_jobs_total_time_report(request):
#     task_times = list(TaskTime.objects.all())

#     # job_type = {
#     #     "spares": [],
#     #     "machines": [],
#     #     "filtec": [],
#     # }

#     # main_job_codes = {}

#     for t in task_times:
#         js = t.job_code.split("-")

#     # Define ranges
#     x_axis = []
#     y_axis = []

#     script, div = get_graph_components(x_axis, y_axis)
#     context = {
#         "script": script,
#         "div": div
#     }
#     return render(request, "partials/totalJobTimeComparison.html", context)


def task_timer_reports(request):
    # Get all task times 
    task_times = list(TaskTime.objects.all())

    # Add up all the time for each job code
    job_code_hours = {}

    for t in task_times:
        if t.job_code not in job_code_hours:
            job_code_hours[t.job_code] = t.elapsed_time
        else:
            job_code_hours[t.job_code] += t.elapsed_time

    # We need lists for the input for the x and y axis's respectively
    jc_list = list(job_code_hours.keys())
    et_list = list(job_code_hours.values())

    # We want the time in hours
    et_list = [t.total_seconds() / 3600 for t in et_list]

    script, div = get_graph_components(jc_list, et_list)

    context = {
        "reports": "Here are some task timer reports",
        "script": script,
        "div": div
    }

    return render(request, "reports/taskTimerPage.html", context)

