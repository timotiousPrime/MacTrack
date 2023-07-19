from django.urls import path

from timesheets import views

urlpatterns = [
    path("", views.task_timer, name="Task_Timer"),
]
