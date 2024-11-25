from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {
        'tasks': tasks
    })

def create (request):
    