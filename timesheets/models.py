from django.db import models
# Get user
from django.contrib.auth.models import User


# Create your models here.
class TaskTime(models.Model):
    JOB_DESCRIPTIONS = [
        ("Adm", "Admin"),
        ("Des", "Design"),
        ("Doc", "Documentation"),
        ("Dwg", "Drawings"),
        ("Gen", "General"),
    ]

    job_code = models.CharField(max_length=16, default="General", null=False, blank=False)
    description = models.CharField(max_length=3, default="Gen", choices=JOB_DESCRIPTIONS, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    elapsed_time = models.TimeField(blank=True, null=True)
    time_started = models.DateTimeField(blank=True, null=True)
    time_stopped = models.DateTimeField(blank=True, null=True)
    is_timing = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self) -> str:
        return self.jobCode + ': ' + str(self.times_spent)