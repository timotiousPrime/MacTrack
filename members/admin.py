from django.contrib import admin
from .models import User_Profile
from django.contrib.auth.models import User

# Unregister initial users
admin.site.unregister(User)

# Register your models here.
admin.site.register(User, User_Profile)

class ProfileInline(admin.StackedInline):
    model = User_Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]