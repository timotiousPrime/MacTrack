from django import forms
from django.contrib.auth.models import User
from members.models import User_Profile


# Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field


class Login_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class New_User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")    

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "my-2 form-control",
                    "placeholder": "username",
                }
            ),
            "password": forms.TextInput(
                attrs={
                    "class": "my-2 form-control",
                    "placeholder": "password",
                    'type': 'password',
                }
            ),
        }

    def __init__(self,*args, **kwargs):
        super(New_User_Form, self).__init__(*args, **kwargs)
        
        # Crispy
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-verticle'

        self.helper.add_input(Submit('submit', 'Submit'))


class User_Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ('firstName', 'lastName', 'role')

        widgets = {
            "firstName": forms.TextInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "First Name",
                }
            ),
            "lastName": forms.TextInput(
                attrs={
                    "class": "my-2 form-control",
                    "placeholder": "Last Name",
                    'type': 'text',
                }
            ),
            "role": forms.Select(
                attrs={
                    "class": "my-2 form-select",
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "my-2 form-checkbox",
                }
            ),
        }

        def __init__(self,*args, **kwargs):
            super(New_User_Form, self).__init__(*args, **kwargs)
            
            # Crispy
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.form_class = 'form-verticle'



class Edit_User_Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ('firstName', 'lastName', 'role', 'is_active')

        widgets = {
            "firstName": forms.TextInput(
                attrs={
                    "class": "my-2 form-control",
                    "placeholder": "First Name",
                }
            ),
            "lastName": forms.TextInput(
                attrs={
                    "class": "my-2 form-control",
                    "placeholder": "Last Name",
                    'type': 'text',
                }
            ),
            "role": forms.Select(
                attrs={
                    "class": "mt-2 mb-3 form-select",
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-checkbox",
                }
            ),
        }

        def __init__(self,*args, **kwargs):
            super(New_User_Form, self).__init__(*args, **kwargs)
            
            # Crispy
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.form_class = 'form-verticle'