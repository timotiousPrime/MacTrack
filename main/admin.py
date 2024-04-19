from django.contrib import admin
from members.models import User_Profile
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = User_Profile
    can_delete = False
    verbose_name_plural = 'user profile'
    fields = ['first_name', 'surname', 'role', 'is_active']


class UserAdmin(BaseUserAdmin):
    model = User
    inlines = [UserProfileInline]

# Unregister initial User so we can update the modified User for admin
admin.site.unregister(User)
admin.site.unregister(Group)
# Reregister User and profile
admin.site.register(User, UserAdmin)