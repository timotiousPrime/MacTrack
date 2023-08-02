from django.urls import path

from projects import views

urlpatterns = [
    path("", views.projects_landing_page, name="Projects_Page"),
]
