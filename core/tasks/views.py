from core.tasks.models import Task
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from core.tasks.forms import TaskForm
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView, ListView

# https://docs.djangoproject.com/en/5.1/ref/class-based-views/

class TaskView(TemplateView):
    template_name = "create_task.html"
    form_class = TaskForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            
            return JsonResponse({"status": 200, "message": "Task was created!"})

        return JsonResponse({"status": 400, "message": form.errors})

class ListTasks(ListView):
    model = Task
    template_name = "list_task.html"

class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy("list-task")
    template_name = "task_confirm_delete.html"