import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, generics, parsers

from core.tasks.models import Task
from core.tasks.file_loader import handle_file
from core.tasks.api.serializers import TaskSerializer, TaskUploadSerializer


logger = logging.Logger("Tasks API")

class TaskAPIView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)

class FileUploadTaskAPIView(generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUploadSerializer
    parser_classes = (parsers.MultiPartParser,)
    
    def post(self, request, *args, **kwargs):
        file = request.FILES.get("file", None)
        
        if not file:
            logger.error("API requires a File.")
            return Response(
                {
                    "message": "Invalid file.",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
            
        return handle_file(file)