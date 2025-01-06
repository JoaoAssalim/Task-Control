from core.tasks.models import Task
from rest_framework import viewsets
from core.tasks.api.serializers import TaskSerializer

class TaskAPIView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    # next step is to customize the post method