from datetime import timedelta, datetime
from django.utils import timezone
from django import template

register = template.Library()

@register.filter
def isEditable(value):
    now = timezone.now()
    aWeekAgo = now-timedelta(days=7)
    print(value, type(value), type(aWeekAgo))
    return value > aWeekAgo

