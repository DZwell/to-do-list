"""Django views."""
from django.shortcuts import render, redirect, get_object_or_404
import datetime
from .models import Task
from .form import TaskForm


def home_view(request, **kwargs):
    """Return home page."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        new_task = Task(task=form.data['task'], notes=form.data['notes'])
        new_task.created = datetime.datetime.utcnow()
        new_task.save()
    tasks = Task.objects.order_by('id')
    form = TaskForm()
    return render(request, 'index.html', {'form': form, 'tasks': tasks})


def delete_task(request, **kwargs):
    """Delete task."""
    import pdb;pdb.set_trace()
    if request.GET.get('delete'):
        task = Task(pk=kwargs['pk'])
        task.delete()
        return redirect('/')


def edit_task(request, pk):
    """Edit task."""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            task.task = form['task'].data
            task.notes = form['notes'].data
            task.created = datetime.datetime.utcnow()
            task.save()
        return redirect('home_view')
    form = TaskForm(instance=task)
    all_tasks = Task.objects.order_by('id')
    return render(request, 'index.html', {'form': form, 'task': task, 'tasks': all_tasks})



