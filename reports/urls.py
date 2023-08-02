from django.urls import path

from reports import views

urlpatterns = [
    path("", views.reports_landing_page, name="Reports_Page"),
    path("taskTimers/", views.task_timer_reports, name='Task_Timer_Reports'),
]
