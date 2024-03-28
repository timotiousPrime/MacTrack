from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_Profile(models.Model):
    USER_ROLE = [
        ("Des", "Designer"),
        ("Man", "Manager"),
        ("Fit", "Fitter"),
        ("Mac", "Machinist"),
        ("Adm", "Admin"),
        ("Gen", "General"),
        ("Ele", "Electrician"),
        ("Wel", "Welder"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    firstName = models.CharField(max_length=48, null=True, blank=True)
    lastName = models.CharField(max_length=48, null=True, blank=True)
    role = models.CharField(max_length=3, choices=USER_ROLE, default="Gen")
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.username
    
