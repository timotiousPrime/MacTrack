from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from projects.forms import ProjectForm
from projects.models import Project
from django.contrib.auth.models import User

# Create your views here.

def projects_landing_page(request):
    projects = Project.objects.all()
    context = {
        "projects_form": ProjectForm,
        "projects": projects
    }
    return render(request, "projects/projectsPage.html", context)

def create_Project(request):
    if request.method == "POST":
        user = get_object_or_404(User, username=request.user.username)
        form = ProjectForm(request.POST)
        if form.is_valid:
            project = form.save(commit=False)
            project.created_by = user
            project.save()
            return redirect("Projects_Page")
        
    context = {
        "projects_form": ProjectForm
    }
    return render(request, 'projects/addProject.html', context)