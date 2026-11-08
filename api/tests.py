from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class HealthEndpointTests(APITestCase):
    def test_health_returns_ok(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "ok")
        self.assertIn("commit", response.data)


class HelloEndpointTests(APITestCase):
    def test_hello_defaults_to_world(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Hello, World!")

    def test_hello_uses_name_param(self):
        response = self.client.get(reverse("hello"), {"name": "Gio"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Hello, Gio!")


class IndexEndpointTests(APITestCase):
    def test_root_redirects_to_api_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response["Location"], "/api/")

        

class AddEndpointTests(APITestCase):
    def test_add_returns_sum(self):
        response = self.client.get(reverse("add"), {"a": 2, "b": 3})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["result"], 5)
