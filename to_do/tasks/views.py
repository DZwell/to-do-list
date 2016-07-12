"""Django views."""
from django.shortcuts import render
from .models import Task
from .form import TaskForm


def home_view(request):
    """Return home page."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        new_task = Task(task=form.data['task'], notes=form.data['notes'])
        new_task.save()
        return render(request, 'index.html')
    form = TaskForm()
    return render(request, 'index.html', {'form': form})

