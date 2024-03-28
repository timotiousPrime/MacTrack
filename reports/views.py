from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils import timezone
from django.http import HttpResponseNotAllowed

from reports.utilities import getDesignerTaskTimeChartContext, getAdminProjectTimesChartContext, testGraph
from reports.forms import adminProjectTaskTimeFilterForm

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
    userId = request.user.id
    context = getDesignerTaskTimeChartContext(userId)

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

@login_required
@user_passes_test(admin_check, login_url='/reports/taskTimers/')
def project_task_chart(request):
    if request.method == "GET":
        context = getAdminProjectTimesChartContext()
        return render(request, "reports/projectTaskChart.html", context)
    if request.method == "POST":
        print("****************************************************************** POST ******************************************************************")
        form = adminProjectTaskTimeFilterForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("form is valid")
            print("Form job_code: ", form.cleaned_data["job_code"])
            print("Form ancillary_code: ", form.cleaned_data["ancillary_code"])
            print("Form user: ", form.cleaned_data["user"])
            context = getAdminProjectTimesChartContext(input)

            return render(request, "reports/projectTaskChart.html", context)
        else:
            print("Form is not valid")
            context = getAdminProjectTimesChartContext(input)
            return render(request, "reports/projectTaskChart.html", context)
    
    return HttpResponseNotAllowed(['GET', 'POST'])

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

def testing_view(request):
    context = testGraph()
    return render(request, "reports/testingPage.html", context)