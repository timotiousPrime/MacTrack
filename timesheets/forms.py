from django import forms
from timesheets.models import TaskTime
from django.utils import timezone


class Task_Timer_Form(forms.ModelForm):
    class Meta:
        model = TaskTime
        fields = ("job_code", "description", "elapsed_time")

        widgets = {
            "job_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Job Code",
                }
            ),
            "description": forms.Select(attrs={"class": "form-select"}),
            "elapsed_time": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "pattern": "\d{2}:\d{2}",
                    "title": "Enter duration in the format: HH:MM",
                    "id": "elapsed_time_input",
                    "name": "time",
                    "value": "00:00",
                }
            ),
        }


# class User_Profile(forms.ModelForm):
#     class Meta:
#         model = User_Profile
#         fields = ('firstName', 'lastName', 'role', 'is_active')

#         # widgets = {
#         #     'firstName': forms.TextInput(attrs={'class': 'form-control'}),
#         #     'lastName': forms.TextInput(attrs={'class': 'form-control'}),
#         #     'role': forms.Select(attrs={'class': 'form-control'}),
#         #     'is_active': forms.BooleanField(attrs={'class': 'form-control'}),
#         # }
