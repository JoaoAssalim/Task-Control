from django.urls import reverse
from django.test import TestCase
from core.tasks.models import Task
from django.contrib.auth import get_user_model


User = get_user_model()


class TestTaskModel(TestCase):
    def setUp(self):
        user = User.objects.create(username="test")
        Task.objects.create(name="Task 1", status="waiting", created_by=user)

    def test_get_task(self):
        task = Task.objects.get(name="Task 1")
        self.assertEqual(task.name, "Task 1")
        self.assertEqual(task.status, "waiting")
    
    def test_create_task(self):
        user = User.objects.get(username="test")
        task = Task.objects.create(name="Task 2", status="waiting", created_by=user)
        self.assertEqual(task.name, "Task 2")
        self.assertEqual(task.status, "waiting")
    
    def test_delete_task(self):
        task = Task.objects.get(name="Task 1")
        task.delete()
        self.assertEqual(Task.objects.count(), 0)


class TestTasksViews(TestCase):
    def test_get_task_form(self):
        response = self.client.get(reverse("create-task"))
        self.assertEqual(response.status_code, 200)
    
    def test_create_task(self):
        user = User.objects.create(username="test")
        self.client.force_login(user)
        response = self.client.post(reverse("create-task"), {"name": "Task 1", "status": "waiting"})
        self.assertEqual(response.status_code, 200)
    
    def test_delete_task(self):
        user = User.objects.create(username="test")
        self.client.force_login(user)
        task = Task.objects.create(name="Task 1", status="waiting", created_by=user)
        response = self.client.delete(reverse("delete-task", args=[task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("list-task"))

    
    def test_list_all_tasks(self):
        response = self.client.get(reverse("list-task"))
        self.assertEqual(response.status_code, 200)
