from django.urls import path
from rest_framework import routers
from core.tasks.api.views import TaskAPIView, FileUploadTaskAPIView

# look for diference between some routers
router = routers.DefaultRouter()
router.register(r'task', TaskAPIView)

urlpatterns = [
    path("task/upload", FileUploadTaskAPIView.as_view())
]

urlpatterns += router.urls