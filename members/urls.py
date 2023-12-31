from django.urls import path

from members import views

urlpatterns = [
    path("login/", views.login_view, name="Login"),
    path("logout/", views.logout_view, name="Logout"),
    path("<str:username>/", views.user_profile, name="User_Profile"),
    path("<str:username>/taskHistory", views.user_task_history, name="User_Task_History"),
]
