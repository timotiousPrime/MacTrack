from django.db import models

# Get user
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.
class TaskTime(models.Model):
    JOB_DESCRIPTIONS = [
        ("Adm", "Admin"),
        ("Des", "Design"),
        ("Doc", "Documentation"),
        ("Dwg", "Drawings"),
        ("Gen", "General"),
    ]

    job_code = models.CharField(
        max_length=16, null=False, blank=False
    )
    description = models.CharField(
        max_length=3, default="Gen", choices=JOB_DESCRIPTIONS, null=False, blank=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    elapsed_time = models.DurationField(blank=True, null=True)
    time_started = models.DateTimeField(blank=True, null=True)
    time_stopped = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    is_running = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.job_code + ": " + str(self.elapsed_time)

    def get_elapsed_time(self):
        """Get elapsed time of task"""
        started = self.time_started
        stopped = self.time_stopped

        if started and stopped:
            # Format the elapsed_time as (hrs, min, seconds)
            recent_elapsed_time = self.time_stopped - self.time_started

            if self.elapsed_time:
                total_elapsed_time = self.elapsed_time + recent_elapsed_time
            else:
                total_elapsed_time = recent_elapsed_time

            # Convert the total_elapsed_time (which is a timedelta object) to minutes and hours
            minutes, seconds = divmod(total_elapsed_time.seconds, 60)
            hours, minutes = divmod(minutes, 60)

            # convert the timedelta to time format and save to the object
            total_elapsed_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)

            self.elapsed_time = total_elapsed_time
            self.save()  # Don't forget to save the changes

            # return the time difference in formatted
            return total_elapsed_time

        return self.elapsed_time
