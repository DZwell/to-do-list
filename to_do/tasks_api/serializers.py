"""Serializers file."""

from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    """Task Serializer."""

    class Meta:
        """Meta."""

        model = Task
        fields = '__all__'
