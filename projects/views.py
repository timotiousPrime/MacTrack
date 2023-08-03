from django.shortcuts import render
from projects.forms import ProjectForm
from projects.models import Project
# Create your views here.

def projects_landing_page(request):
    projects = Project.objects.all()
    context = {
        "projects_form": ProjectForm,
        "projects": projects
    }
    return render(request, "projects/projectsPage.html", context)

def create_Project(request):
        
    context = {
        "projects_form": ProjectForm
    }
    return render(request, 'projects/addProject.html', context)