"""Django form."""
from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    """Task model form."""

    class Meta:
        """Meta."""

        model = Task
        exclude = []

