import os 

import pandas as pd

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, generics, parsers

from core.tasks.models import Task
from core.tasks.api.serializers import TaskSerializer, TaskUploadSerializer

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
            return Response(
                {
                    "message": "Invalid file.",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
            
        extension = os.path.basename(file.name).split(".")[-1]
            
        if extension not in ["csv", "xlsx"]:
            return Response(
                {
                    "message": "Invalid file extension.",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
            
    
        if extension == "csv":
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
        
        bulk_tasks = [{"name": item.name, "status": item.status, "created_by": item.created_by} for item in df.itertuples()]
        
        serializer = TaskSerializer(data=bulk_tasks, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        
        return Response(
            {
                "message": "File was uploaded with success.",
            },
            status=status.HTTP_201_CREATED
        )