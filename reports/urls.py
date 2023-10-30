from django.urls import path

from reports import views

urlpatterns = [
    path("", views.reports_landing_page, name="Reports_Page"),
    path("taskTimers/", views.task_timer_reports, name='Task_Timer_Reports'),
    path("admin/", views.admin_reports_page, name='Admin_Reports'),
    path("admin/taskTimes", views.full_task_time_report, name='Task_Time_Report'),
]
