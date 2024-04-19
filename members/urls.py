from django.urls import path
from .views import UserListView
from members import views

urlpatterns = [
    path("login/", views.login_view, name="Login"),
    path("logout/", views.logout_view, name="Logout"),
    path("<str:username>/", views.user_profile, name="User_Profile"),
    path("<str:username>/taskHistory", views.user_task_history, name="User_Task_History"),
    path("list", UserListView.as_view(), name="User_List"),
    path("add_user", views.addNewUser, name="Add_User"),
    path("edit_user/<str:userId>", views.editUser, name="Edit_User"),
]
