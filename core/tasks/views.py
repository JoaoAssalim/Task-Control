from django.shortcuts import render
from django.http import JsonResponse
from core.tasks.forms import TaskForm
from django.views.generic import TemplateView

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