from django.contrib import admin
from .models import FittingTask


class FittingTaskAdmin(admin.ModelAdmin):
    fields= ['user', 'job_code', 'ancillary_code', 'date_created', 'time_started', 'time_stopped']
    readonly_fields = ['date_created', 'date_edited']
# Register your models here.
admin.site.register(FittingTask, FittingTaskAdmin)
