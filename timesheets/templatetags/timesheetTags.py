from datetime import timedelta, datetime
from django.utils import timezone
from django import template
from django.template.defaultfilters import pluralize

register = template.Library()

@register.filter
def isEditable(value, mode=""):
    now = timezone.now()
    aWeekAgo = now-timedelta(days=7)
    return value > aWeekAgo

