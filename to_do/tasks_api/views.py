from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from tasks.models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Task viewset."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

