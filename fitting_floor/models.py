from django.db import models
from projects.models import Project
from datetime import timedelta
from timesheets.models import AncillaryJobCode
from django.contrib.auth.models import User

# Create your models here.

class FittingTask(models.Model):

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

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="fitting_task")
    notes = models.TextField(max_length=240, blank=True, null=True)
    elapsed_time = models.DurationField(blank=True, null=True)
    time_started = models.TimeField(blank=True, null=True)
    time_stopped = models.TimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    is_running = models.BooleanField(default=False)
    is_ongoing = models.BooleanField(default=True)

    class Meta:
        ordering = ['date_created', 'user']

    def __str__(self) -> str:
        return str(self.user) + ": " + str(self.job_code) + " - " + str(self.elapsed_time)

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
