from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    code = models.CharField(max_length=8, blank=False, null=False, unique=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    fax_number = models.CharField(max_length=13, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    contact_person = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name

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
    is_high_priority = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    job_code = models.CharField(max_length=8, primary_key=True, blank=False, null=False)
    status = models.CharField(max_length=4, default="Des", choices=PROJECT_STATUS, null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    project_captains = models.ManyToManyField(User, related_name="projects")
    purchase_order_number = models.CharField(max_length=24)

    def __str__(self) -> str:
        return self.job_code

