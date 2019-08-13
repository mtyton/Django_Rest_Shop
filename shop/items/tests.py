from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
import os


class TestCategories(TestCase):
    def setUp(self):
        pass

    def test_get_data_no_auth(self):
        url = reverse("categories")
        response = self.client.get(url, format="json")
        print(response)