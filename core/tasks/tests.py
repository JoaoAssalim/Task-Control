from django.test import TestCase
from django.http import HttpRequest
from core.tasks.views import TaskView

# criar testes

# class TesteCBV(TestCase):
#     def test_get(self):
#         request = HttpRequest()
#         request.method = 'POST'
#         response = TaskView.as_view()(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json()['message'], "Requisição GET recebida")