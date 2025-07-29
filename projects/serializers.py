from rest_framework import serializers
from .models import Project, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at', 'tasks']
        read_only_fields = ['id', 'created_at']

