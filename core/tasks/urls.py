from django.urls import path

from core.tasks.views import TaskView

urlpatterns = [
    path('create-task/', TaskView.as_view())
]
