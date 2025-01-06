from django import forms
from core.tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = [
            "name",
            "status",
        ]