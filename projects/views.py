from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from projects.forms import ProjectForm, CustomerForm
from projects.models import Project, Customer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def projects_landing_page(request):
    projects = Project.objects.all()
    context = {
        "title": "Projects",
        "projects_form": ProjectForm,
        "projects": projects
    }
    return render(request, "projects/projectsPage.html", context)

@login_required
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

@login_required
def customers_page(request):
    customers = Customer.objects.all()
    context = {
        "title": "Customers",
        "customers": customers
    }
    return render(request, "projects/customersPage.html", context)

@login_required
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("Customers_Page")
        
    context = {
        "customer_form": CustomerForm
    }
    return render(request, 'projects/addCustomer.html', context)
    