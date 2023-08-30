from django.urls import path

from . import views

urlpatterns = [
    path("", views.landingPage, name="Home"),
    path("login/", views.login_page, name="Log"),
]
