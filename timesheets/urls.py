from django.urls import path

from timesheets import views

urlpatterns = [
    path("", views.task_timer, name="Task_Timer"),
    path("add/", views.create_task, name="Create_Timer"),
    path("start/", views.start_timer, name="Start_Timer"),
    path("stop/", views.start_timer, name="Stop_Timer"),
]
