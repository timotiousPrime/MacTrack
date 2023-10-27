from django.contrib.auth.models import User
from timesheets.models import TaskTime
from members.models import User_Profile



# Utility functions for report views

def adminReportsContext():
    designers = User_Profile.objects.filter(role="Des")
    
    designersTaskTimes = {}

    for designer in designers:
        designerTaskTimes = TaskTime.objects.filter(user=designer.user.id)
        designersTaskTimes[designer] = designerTaskTimes
    
    print(designersTaskTimes)

    # Designer Task Times Stats
    # {"Designer": DesignerUsername, "ProjectCount": TotalProjects, "AccumulatedMonthlyTime"}
    
    return {
        "title": "Admin Reports",
        "designers": designers,
        "designerTaskTimes": designersTaskTimes

    }