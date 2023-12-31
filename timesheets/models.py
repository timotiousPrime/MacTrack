from django.db import models
from projects.models import Project
from datetime import timedelta

# Get user
from django.contrib.auth.models import User


# Create your models here.
class AncillaryJobCode(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    description = models.CharField(max_length=42)

    class Meta:
        ordering = ['description']

    def __str__(self):
        return self.description
    

class TaskTime(models.Model):
    JOB_DESCRIPTIONS = [
        ("Adm", "Admin"),
        ("Des", "Design"),
        ("Doc", "Documentation"),
        ("Dwg", "Drawings"),
        ("Gen", "General"),
        ("Mod", "Modifications"),
    ]

    job_code = models.ForeignKey(
        Project, 
        null=False, 
        blank=False,
        on_delete=models.PROTECT,
        limit_choices_to={"is_active": True}
    )
    ancillary_code = models.ForeignKey(
        AncillaryJobCode,  
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
    )
    description = models.CharField(
        max_length=3, default="Gen", choices=JOB_DESCRIPTIONS, null=False, blank=False
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="tasks")
    elapsed_time = models.DurationField(blank=True, null=True)
    time_started = models.DateTimeField(blank=True, null=True)
    time_stopped = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    is_running = models.BooleanField(default=False)
    is_ongoing = models.BooleanField(default=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self) -> str:
        return str(self.job_code) + ": " + str(self.elapsed_time)
    
    def get_description_count(self):
        return len(self.JOB_DESCRIPTIONS)
    
    def get_descriptions(self):
        return [desc[0] for desc in self.JOB_DESCRIPTIONS]

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
