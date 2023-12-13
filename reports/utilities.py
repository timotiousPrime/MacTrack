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
    
    # get a list of all projects user has worked on (no duplicates and ordered alphabetically)
    jobTasksSet = set()

    for task in userTasks:
        jobTasksSet.add(str(task.job_code))

    jobTasksList = list(jobTasksSet)    
    jobTasksList.sort()

    # create dictionary to store total time per description per ancillary code per project
    # jobTasks = {
    #     "jobCode": {
    #         "ancillaryCode": {
    #             "description": "elapsedTime"
    #         }
    #     }
    # }

    jobTasks = {}

    for job in jobTasksList:
        jobTasks[job] = {}

    for job in jobTasks:
        for task in userTasks:
            if job == str(task.job_code):
                key = str(task.ancillary_code)
                descKey = str(task.description)
                if not key in jobTasks[job]:
                    jobTasks[job][key] = {}
                    jobTasks[job][key][descKey] = round(task.elapsed_time.total_seconds()/3600, 1)
                elif key in jobTasks[job] and descKey in jobTasks[job][key]: 
                    jobTasks[job][key][descKey] += round(task.elapsed_time.total_seconds()/3600, 1)
                else:
                    jobTasks[job][key][descKey] = round(task.elapsed_time.total_seconds()/3600, 1)

    # Factors is a list of tuples 
    # each tuple represents a column
    # the first value in the tuple represents the project(group) and the second value represents the ancillary task (column)
    factors = []
    for job in jobTasks:
        for task in jobTasks[job]:
            factors.append((job, task))

    factors.sort(key=lambda x: x[1])
    factors.sort(key=lambda x: x[0])

    descriptionList = userTasks[0].get_descriptions()

    descriptionList.sort()

    # See Bokeh Stacked bar graph documentation for how it needs the data structured
    data = {}

    data["colData"] = factors

    for desc in descriptionList:
        data[desc] = []
        for f in factors:
            if desc in jobTasks[f[0]][f[1]]:
                data[desc].append(jobTasks[f[0]][f[1]][desc])
            else:
                data[desc].append(0)

    script, div = get_stacked_graph_components(factors, descriptionList, data)

    context = {
        "title": "Designer Task Reports",
        "script": script,
        "div": div
    }

    # projects, taskDescriptions, taskTypeTimes 
    return context