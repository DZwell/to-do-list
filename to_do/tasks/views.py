"""Django views."""
from django.shortcuts import render
from .models import Task
from .form import TaskForm


def home_view(request):
    """Return home page."""
    form = TaskForm()
    if request.method == 'POST':
        return
    return render(request, 'index.html', {'form': form})


# def create_task(request):
#     if request.method == 'POST':
