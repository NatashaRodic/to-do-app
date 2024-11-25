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
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todolist')  # Redirect to the task list after saving
    else:
        form = TaskForm()
    return render(request, 'create.html', {'form': form})
