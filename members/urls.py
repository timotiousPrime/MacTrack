from django.urls import path

from members import views

urlpatterns = [
    path("login/", views.login_view, name="Login"),
    path("logout/", views.logout_view, name="Logout"),
    path("<str:username>/", views.userProfile, name="User_Profile"),
]
