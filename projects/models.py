from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    code = models.CharField(max_length=8)
    phone_number = models.CharField(max_length=13)
    fax_number = models.CharField(max_length=13)
    email = models.EmailField()
    contact_person = models.CharField(max_length=40)



class Project(models.Model):
    PROJECT_STATUS = [
        ("Des", "At Design"),
        ("Prod", "In Production"),
        ("Hold", "On Hold"),
        ("Assy", "At Assembly"),
        ("Awt", "Awaiting Delivery"),
        ("Del", "Delivered"),
        ("Can", "Cancelled"),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    description = models.CharField(max_length=144)
    isHighPriority = models.BooleanField(default=False)
    job_code = models.CharField(max_length=8, primary_key=True, blank=False, null=False)
    status = models.CharField(max_length=4, default="Des", choices=PROJECT_STATUS, null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    project_captains = models.ManyToManyField(User, related_name="projects")
    purchase_order_number = models.CharField(max_length=24)

