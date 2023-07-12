from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import User_Profile

admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
    model = User_Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]


# Unregister initial users
admin.site.unregister(User)

# Register your models here.
admin.site.register(User, UserAdmin)
