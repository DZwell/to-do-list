"""Django form."""
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """Task model form."""

    class Meta:
        """Meta."""

        model = Task
        widgets = {
            'task': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            # 'notes': forms.TextInput(attrs)
        }
        exclude = []

