from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
# Create your tests here.
class Tests(APITestCase):
    def test_status_returns_200(self):
        response = self.client.get('/api/hello/')
        self.assertEqual(response.status_code, 200)

    def test_message_returns(self):
        response = self.client.get('/api/hello/')
        self.assertEqual(response.data["message"], "Hello")
