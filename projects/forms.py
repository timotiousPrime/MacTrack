from django import forms
from projects.models import Project, Customer
from django.utils import timezone


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "job_code", 
            "customer", 
            "purchase_order_number",
            "description", 
            "is_high_priority", 
            "project_captains", 
        )

        widgets = {
            "job_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Job Code",
                }
            ),
            "customer": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Customer",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control", 
                    "placeholder": "Project Description"
                }
            ),
            "purchase_order_number": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "project_captains": forms.SelectMultiple(
                attrs={
                    "class": "form-select select2",
                    "placeholder": "Captains",
                }
            ),
            "is_high_priority": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "name", 
            "code", 
            "phone_number",
            "email", 
            "contact_person", 
        )

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Customer Name",
                }
            ),
            "code": forms.TextInput(
                attrs={
                    "class": "form-control", 
                    "placeholder": "Customer Code"
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control", 
                    "placeholder": "Phone Number"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control", 
                    "placeholder": "Email"
                }
            ),
            "contact_person": forms.TextInput(
                attrs={
                    "class": "form-control", 
                    "placeholder": "Contact Person"
                }
            ),
        }        