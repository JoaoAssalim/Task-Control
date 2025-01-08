from django.urls import path

from core.tasks.views import TaskView, ListTasks, DeleteTask

urlpatterns = [
    path('create-task/', TaskView.as_view(), name="create-task"),
    path('list-task/', ListTasks.as_view(), name="list-task"),
    path('delete-task/<int:pk>', DeleteTask.as_view(), name="delete-task")
]
