from django.urls import path

from projects import views

urlpatterns = [
    path("", views.projects_landing_page, name="Projects_Page"),
    path("add/", views.create_Project, name="Create_Project"),
    path("customers/", views.customers_page, name="Customers_Page"),
    path("add_customer/", views.add_customer, name="Add_Customer"),
]
