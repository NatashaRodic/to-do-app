from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {
        'tasks': tasks
    })

def create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('')
    return render(request, 'create.html', {'form': form})

def details(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'details.html', {
        'task': task
    })

def update(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('')
    return render(request, 'update.html', {'form': form, 'task': task})