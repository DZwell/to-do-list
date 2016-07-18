from django.shortcuts import render
from rest_framework import viewsets
from tasks.models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Task viewset."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer()
