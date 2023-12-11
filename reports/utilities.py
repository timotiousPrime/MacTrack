from django.shortcuts import render
from datetime import timedelta

# Models 
from django.contrib.auth.models import User
from timesheets.models import TaskTime
from members.models import User_Profile

# Import graph components
from .templates.graphs.barChart import get_graph_components, get_stacked_graph_components

# Utility functions for report views

def adminReportsContext():
    
    tasks = TaskTime.objects.all().exclude(elapsed_time = timedelta(seconds=0)).order_by("-date_created", "user", "job_code", "ancillary_code", "description")[:5]

    return {
        "title": "Admin Reports",
        "tasks": tasks
    }

def designerReportContext():
    # Get all task times 
    task_times = list(TaskTime.objects.all())

    # Add up all the time for each job code
    job_code_hours = {}

    for t in task_times:
        if t.job_code not in job_code_hours:
            job_code_hours[str(t.job_code)] = t.elapsed_time
        else:
            job_code_hours[str(t.job_code)] += t.elapsed_time

    # We need lists for the input for the x and y axis's respectively
    jc_list = list(job_code_hours.keys())
    et_list = list(job_code_hours.values())

    # We want the time in hours
    if et_list is not None:
        et_list = [t.total_seconds() / 3600 for t in et_list]
    else:
        et_list = []


    script, div = get_graph_components(jc_list, et_list)

    context = {
        "title": "Task Timer Reports",
        "reports": "Here are some task timer reports",
        "script": script,
        "div": div
    }

    return context

def getDesignerTaskTimeChartContext(userId):
    userTasks = TaskTime.objects.filter(user=userId)
    jobTasks = set()            # {(job_code, ancillary_code),} --> these are the tasks that will be the column of the graph
    taskDescriptions = set()    # {task.description,} --> these is what the column of the graph will be divided into **This will be converted to a list
    taskTypes = set()           # {(job_code, ancillary_code, description),} --> this is a unique list of the tasks per jc, anc, and desc used to get the total time 
    uniqueTaskTimes = {}         # {'job_code-ancillary_code-description': total elapsed time,}
    taskTypeTimes = {}          # {'description': list of total time of description per jobTask,}

    for task in userTasks:
        jobTaskTuple = (str(task.job_code), str(task.ancillary_code)) 
        taskTypeTuple = (str(task.job_code), str(task.ancillary_code), str(task.description))
        taskDescriptions.add(str(task.description))
        jobTasks.add (jobTaskTuple)
        taskTypes.add (taskTypeTuple)
        taskType = str(task.job_code) + "-" + str(task.ancillary_code) + "-" + str(task.description)
        if taskType in uniqueTaskTimes:
            uniqueTaskTimes[taskType] += round(task.elapsed_time.total_seconds()/3600, 1) # hours
        else:
            uniqueTaskTimes[taskType] = round(task.elapsed_time.total_seconds()/3600, 1) # hours

    # Convert jobTask set into a list of strings
    jobs = [task[0] + "-" + task[1] for task in jobTasks] 
    taskTypeTimes["description"] = jobs
    
    for desc in taskDescriptions:
            taskTypeTimes[desc] = []
            for task in jobTasks:
                taskType = task[0] + "-" + task[1] + "-" + desc
                if taskType in uniqueTaskTimes:
                    taskTypeTimes[desc].append(uniqueTaskTimes[taskType])
                else:
                    taskTypeTimes[desc].append(0)



    script, div = get_stacked_graph_components(jobs, taskDescriptions, taskTypeTimes)

    context = {
        "title": "Designer Task Reports",
        "script": script,
        "div": div
    }

    # projects, taskDescriptions, taskTypeTimes 
    return context