from django.contrib import admin
from timesheets.models import TaskTime
from django.contrib.auth.models import User
from .models import User_Profile

# Register your models here.

admin.site.register(TaskTime)

# class ProfileInline(admin.StackedInline):
#     model = User_Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "email"]
    # inlines = [ProfileInline]


# Unregister initial User so we can update the modified User for admin
admin.site.unregister(User)

# Reregister User and profile
admin.site.register(User, UserAdmin)
admin.site.register(User_Profile)