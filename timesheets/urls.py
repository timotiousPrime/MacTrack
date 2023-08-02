from django.urls import path

from timesheets import views

urlpatterns = [
    path("", views.task_timer, name="Task_Timer"),
    path("add/", views.create_task, name='Create_Timer'),
    path("start/<int:task_id>", views.start_timer, name='Start_Timer'),
    path("stop/<int:task_id>", views.stop_timer, name='Stop_Timer'),
    path("edit/<int:task_id>", views.edit_timer, name='Edit_Timer'),
    path("delete/<int:task_id>", views.delete_timer, name='Delete_Timer'),
]
