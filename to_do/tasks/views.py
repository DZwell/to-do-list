"""Django views."""
from django.shortcuts import render, redirect
from .models import Task
from .form import TaskForm


def home_view(request):
    """Return home page."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        new_task = Task(task=form.data['task'], notes=form.data['notes'])
        new_task.save()
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'index.html', {'form': form, 'tasks': tasks})


def delete_task(request, **kwargs):
    """Delete task."""
    task = Task.objects.get(pk=kwargs['pk'])
    task.delete()
    return redirect('/')



