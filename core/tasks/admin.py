from django.contrib import admin
from core.tasks.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_at", "created_by")


admin.site.register(Task, TaskAdmin)