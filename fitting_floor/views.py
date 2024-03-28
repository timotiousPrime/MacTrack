from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.db import transaction

from members.models import User_Profile
from .models import FittingTask
from .forms import Fitting_Task_Form, Fitting_Task_Edit_Form
# Generic Class Views
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.
def get_fitters_task_list():
    fitters_list = User_Profile.objects.filter(role='Fit').order_by('firstName')
    fitters_tasks = []
    today = timezone.localdate()

    print(today)
    for fitter in fitters_list:
        fitter_task_list = []
        for task in fitter.user.fitting_task.filter(date_created__date=today):
            fitter_task_list.append(task)

        fitters_tasks.append((fitter.user.username, fitter_task_list))
    
    return fitters_tasks

@login_required
def fitting_floor_home(request):
    form = Fitting_Task_Form

    context = {
        "title": "Fitting Floor",
        "form": form,
        "fitters": get_fitters_task_list(),
    }
    return render(request, "fitting_floor/fittingFloorHome.html", context)


class DeleteFittingTask(DeleteView):
    model = FittingTask
    success_url = reverse_lazy("ff:Fitting_Floor")
    template_name = "fitting_floor/deleteFittingTaskPage.html"


def addFittingTask(request):
    context = {
        "title": "Fitting Floor",
        "form": Fitting_Task_Form(),   
        "fitters_list": get_fitters_task_list()
    }
    if request.method == 'POST':
        form = Fitting_Task_Form(request.POST)
        if form.is_valid():
            form.save()
            context['form'] = form
            return redirect("ff:Fitting_Floor")
        # Add failed message here
        print("Form errors: ",form.errors)
        return redirect("ff:Fitting_Floor")
    

class UpdateFittingTask(UpdateView):
    template_name = "fitting_floor/updateFittingTaskPage.html"
    model = FittingTask
    fields = ["user", "job_code", "ancillary_code", "time_started", "time_stopped", "notes"]
    success_url = reverse_lazy('ff:Fitting_Floor')

    def get(self, request, *args, **kwargs):
        print("******The GET method has been called******")
        return render(request, "ff:Edit_Floor_Task", {"form": Fitting_Task_Edit_Form})
    

def updateFittingTask(request, taskId):
    # return HttpResponse(status=200)
    task = FittingTask.objects.get(pk=taskId)
    if request.method == "POST":
        form = Fitting_Task_Edit_Form(request.POST)
        if form.is_valid:
            form.save()
            return redirect("ff:Fitting_Floor")
        
    context = {
        "customer_form": Fitting_Task_Edit_Form(instance=task)
    }
    print("*****THE GET METHOD HAS BEEN CALLED*****")
    return render(request, 'fitting_floor/updateFittingTaskPage.html', context)
    