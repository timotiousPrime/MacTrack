from django.urls import path

from members import views

urlpatterns = [
    path("login/", views.loginView, name="login"),
    path("logout/", views.logoutView, name="logout"),
    path("<str:username>/", views.userProfileView, name="userProfile"),
    path("<str:username>/update/", views.userProfileView, name="postUserProfileUpdate")
]
