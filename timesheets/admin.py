from django.contrib import admin
from timesheets.models import  AncillaryJobCode

# Register your models here.
@admin.register(AncillaryJobCode)
class AncillaryCode(admin.ModelAdmin):
    list_display = ("code", "description")