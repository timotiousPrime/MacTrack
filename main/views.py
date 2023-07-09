from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landingPage(request):
    context = {'greeting': "Welcome to the landing page!"}
    return render(request, 'main/startPage.html', context)