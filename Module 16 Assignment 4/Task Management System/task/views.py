from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.

def task_add(request):
    if request.method == "POST":
        task_from = TaskFrom(request.POST)
        if task_from.is_valid():
            task_from.save()
            print(task_from.cleaned_data)
            return redirect('tasks_view')
    else:
        task_from = TaskFrom()
    return render(request, 'task_add.html', {'from': task_from})

def tasks_view(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task_view.html', {'tasks': tasks})

def task_delete(request, id):
    task =  TaskModel.objects.get(pk=id).delete()
    return redirect('tasks_view')

def task_edit(request, id):
    task = TaskModel.objects.get(pk=id)
    task_from = TaskEditFrom( instance = task)
    if request.method == "POST":
        task_from = TaskEditFrom(request.POST, instance = task)
        if task_from.is_valid():
            task_from.save()
            return redirect('tasks_view')

    return render(request, 'task_edit.html', {'from': task_from})