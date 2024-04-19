from django.urls import path

from fitting_floor import views
from .views import DeleteFittingTask, UpdateFittingTask

app_name = 'ff'

urlpatterns = [
    path("", views.fitting_floor_home, name="Fitting_Floor"),
    path("add_fitting_task", views.addFittingTask, name="Create_Floor_Task"),
    path("edit_task/<int:taskId>", views.testingFF, name="Edit_Floor_Task"),
    path("delete_task/<int:pk>/", DeleteFittingTask.as_view(), name="Delete_Floor_Task"),
]


