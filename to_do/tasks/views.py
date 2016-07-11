"""Django views."""
from django.shortcuts import render
from .models import Task
from .form import TaskForm


def home_view(request):
    """Return home page."""
    form = TaskForm()
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request, 'index.html')
    return render(request, 'index.html', {'form': form})

