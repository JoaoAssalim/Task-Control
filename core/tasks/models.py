from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    STATUS_CHOICES = [
        ("waiting", "Waiting"),
        ("doing", "Doing"),
        ("done", "Done"),
        ("cancelled", "Cancelled")
    ]
    
    name = models.CharField(max_length=125, null=False, blank=False)
    status = models.TextField(choices=STATUS_CHOICES)
    created_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name