from django.shortcuts import render

# Create your views here.

def projects_landing_page(request):
    context = {
        "greeting": "Welcome to the projects page!"
    }
    return render(request, "projects/projectsPage.html", context)