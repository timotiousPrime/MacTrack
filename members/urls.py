from django.urls import path

from members import views

urlpatterns = [
    path("<str:username>/", views.user_profile, name="User_Profile"),
    path("login/", views.login_view, name="Login"),
    path("logout/", views.logout_view, name="Logout"),
]
