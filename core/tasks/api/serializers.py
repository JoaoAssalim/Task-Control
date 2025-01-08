from core.tasks.models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        
class TaskUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    