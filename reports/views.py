from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils import timezone
from reports.utilities import getDesignerTaskTimeChartContext

# Import Utilites
from .utilities import adminReportsContext

# Import graph components
from .templates.graphs.barChart import get_graph_components

# Import app models
from timesheets.models import TaskTime
from members.models import User_Profile

# Create your views here.

def reports_landing_page(request):
    context = {
        "reports": "Here are some reports"
    }
    return render(request, "reports/landingPage.html", context)

def task_timer_reports(request):
    # Get all task times 
    # task_times = list(TaskTime.objects.all())

    # # Add up all the time for each job code
    # job_code_hours = {}

    # for t in task_times:
    #     if t.job_code not in job_code_hours:
    #         job_code_hours[str(t.job_code)] = t.elapsed_time
    #     else:
    #         job_code_hours[str(t.job_code)] += t.elapsed_time

    # # We need lists for the input for the x and y axis's respectively
    # jc_list = list(job_code_hours.keys())
    # et_list = list(job_code_hours.values())


    # # We want the time in hours
    # if et_list is not None:
    #     et_list = [t.total_seconds() / 3600 for t in et_list]
    # else:
    #     et_list = []

    # script, div = get_graph_components(jc_list, et_list)

    # context = {
    #     "title": "Task Timer Reports",
    #     "reports": "Here are some task timer reports",
    #     "script": script,
    #     "div": div
    # }

    context = getDesignerTaskTimeChartContext(request.user.id)

    return render(request, "reports/taskTimerPage.html", context)

def dashboard_project_times_chart(request):
    # Get all user task times
    task_times = list(TaskTime.objects.filter(user=request.user.id))

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
        "reports": "Here are some task timer reports",
        "script": script,
        "div": div
    }

    return render(request, "reports/taskTimerPage.html", context)

# Stacked Barchart for designer tasks times
    # job code and ancillary code as a column
    # column split up by descriptions

# Job tasks
# jobTasks = [jobCodes+ancillaryCodes]
# subTasks = ["Admin", "Design", "Documentation", "Drawings", "General", "Modifications",]

# data = {
# "jobTasks": jobTasks,
# ***dynamically get subTasks as a list with their times*** 
# }

# make a list of all the users jobTasks (job code and ancillary code is one unique jobTask)
# for each jobTask, make a list of all the subTasks and a list of all the subtasks times

# make a dictionary named "data" with jobTasks as a key, the list as the value 
# and then each subTask description as a key and it's total elapsed time as the value

def designer_task_time_charts(request):
    userId = request.user.id
    context = getDesignerTaskTimeChartContext(userId)
    return render(request, "reports/something.html", context)


def admin_check(user):
    userProfile = User_Profile.objects.get(user=user.id)
    return userProfile.role.startswith("Adm")

@login_required
@user_passes_test(admin_check, login_url='/reports/taskTimers/')
def admin_reports_page(request):
    context = adminReportsContext()
    return render(request, "reports/adminReportPage.html", context)


@login_required
@user_passes_test(admin_check, login_url='/reports/taskTimers/')
def full_task_time_report(request):
    context = {
        "title": "Task Times Report",
        "tasks": TaskTime.objects.all().exclude(elapsed_time=None).order_by("-date_created", "user", "job_code", "ancillary_code", "description")
    }
    return render(request, "reports/taskTimeReport.html", context)



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

