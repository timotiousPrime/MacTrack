from django import forms
from timesheets.models import TaskTime

class adminProjectTaskTimeFilterForm(forms.ModelForm):
    class Meta:
        model = TaskTime
        fields = (
            "job_code",
            "ancillary_code",
            "user",
        )
        widgets = {
            "job_code": forms.SelectMultiple(
                    attrs={
                        "class": "form-select select2",
                        "placeholder": "Job Code",
                    }
                ),
            "ancillary_code": forms.SelectMultiple(
                attrs={
                    "class": "form-select select2",
                    "placeholder": "Ancillary Code",
                }
            ),
            "user": forms.SelectMultiple(
                    attrs={
                        "class": "form-select select2",
                        "placeholder": "Designer",
                    }
                ),
        }