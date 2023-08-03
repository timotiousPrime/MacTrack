from django import forms
from timesheets.models import TaskTime
from django.utils import timezone


class Task_Timer_Form(forms.ModelForm):
    class Meta:
        model = TaskTime
        fields = ("job_code", "ancillary_code", "description", "elapsed_time")

        widgets = {
            "job_code": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Job Code",
                }
            ),
            "description": forms.Select(attrs={"class": "form-select"}),
            "ancillary_code": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Ancillary Code",
                }
            ),
            "elapsed_time": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "pattern": "\d{2}:\d{2}:\d{2}",
                    "title": "Enter duration in the format: HH:MM:SS",
                    "id": "elapsed_time_input",
                    "name": "time",
                    "value": "00:00:00",
                }
            ),
        }
