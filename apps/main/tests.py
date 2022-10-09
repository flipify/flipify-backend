from re import A

from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestMain(APITestCase):
    def test_greet_view_response_data_and_status_code(self):
        response = self.client.get(reverse("greet") + "?name=Flipify")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, {"message": "Hello, Flipify!"})
