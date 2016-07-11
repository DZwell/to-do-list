"""Django views."""
from django.shortcuts import render
from .models import Task


def home_view(request):
    """Return home page."""
    return render(request, 'index.html')


# def create_task(request):
#     if request.method == 'POST':
