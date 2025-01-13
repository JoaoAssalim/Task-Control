import json

from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient

from core.tasks.models import Task

class TestChatAPI(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="test", password="test")
        self.client.login(username="test", password="test")
        self.task = Task.objects.create(name="Task 1", status="waiting", created_by=self.user)
    
    def test_create_task(self):
        payload = {"name": "Task 2", "status": "waiting", "created_by": self.user.id}
        response = self.client.post(reverse("task-list"), json.dumps(payload), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 2)
    
    def test_delete_task(self):
        response = self.client.delete(reverse("task-detail", args=[self.task.id]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Task.objects.count(), 0)
    
    def test_list_all_tasks(self):
        response = self.client.get(reverse("task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
    
    def test_get_task(self):
        response = self.client.get(reverse("task-detail", args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Task 1")
    
    def test_update_task(self):
        payload = {"name": "Task 2", "status": "waiting", "created_by": self.user.id}
        response = self.client.patch(reverse("task-detail", args=[self.task.id]), json.dumps(payload), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Task 2")

