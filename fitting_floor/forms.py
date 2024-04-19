from django import forms
from .models import FittingTask
from django.utils import timezone

# Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

# Models 
from django.contrib.auth.models import User
from members.models import User_Profile


class Fitting_Task_Form(forms.ModelForm):
    class Meta:
        model = FittingTask
        # fields = ("user", "job_code", "ancillary_code", "time_started")
        fields = ("user", "job_code", "ancillary_code", "time_started", "time_stopped")

        widgets = {
            "user": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Fitter",
                }
            ),
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
            "time_started": forms.TimeInput(
                attrs={
                    'type': 'time',
                    "class": "form-control",
                }
            ),
            "time_stopped": forms.TimeInput(
                attrs={
                    'type': 'time',
                    "class": "form-control",
                }
            ),
        }

    def __init__(self,*args, **kwargs):
        super(Fitting_Task_Form, self).__init__(*args, **kwargs)
        
        # Crispy
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'

        self.helper.add_input(Submit('submit', 'Submit'))
        
        # Get the User IDs for user profiles where role is 'Fit'
        fitter_user_ids = User_Profile.objects.filter(role="Fit").values_list('user', flat=True)
        
        # Now filter the User queryset to those User IDs
        self.fields['user'].queryset = User.objects.filter(id__in=fitter_user_ids)



class Fitting_Task_Edit_Form(forms.ModelForm):
    class Meta:
        model = FittingTask
        # fields = ("user", "job_code", "ancillary_code", "time_started")
        fields = ("user", "job_code", "ancillary_code", "time_started", "time_stopped", "notes")

        widgets = {
            "user": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Fitter",
                }
            ),
            "job_code": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Job Code",
                }
            ),
            "description": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Desription",
                }
            ),
            "ancillary_code": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Ancillary Code",
                }
            ),
            "time_started": forms.TimeInput(
                attrs={
                    'type': 'time',
                    "class": "form-control",
                }
            ),
            "time_stopped": forms.TimeInput(
                attrs={
                    'type': 'time',
                    "class": "form-control",
                }
            ),
            "notes": forms.TextInput(
                attrs={
                    'type': 'text-area',
                    "class": "form-control",
                }
            ),
            
        }

    def __init__(self,*args, **kwargs):
        super(Fitting_Task_Edit_Form, self).__init__(*args, **kwargs)
        
        # Crispy
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-verticle'

        self.helper.add_input(Submit('submit', 'Submit'))
        
        # Get the User IDs for user profiles where role is 'Fit'
        fitter_user_ids = User_Profile.objects.filter(role="Fit").values_list('user', flat=True)
        
        # Now filter the User queryset to those User IDs
        self.fields['user'].queryset = User.objects.filter(id__in=fitter_user_ids)
