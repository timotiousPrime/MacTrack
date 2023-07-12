from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=48, null=True, blank=True)
    lastName = models.CharField(max_length=48, null=True, blank=True)
    role = models.CharField(max_length=3, choices=USER_ROLE, default="Gen")
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user | "No username saved"
    

def create_profile(sender, instance, created, **kwargs):
    if created:
        userProfile = User_Profile(user=instance)
        userProfile.save()

post_save.connect(create_profile, sender=User)