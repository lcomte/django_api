from django.test import TestCase, Client, RequestFactory

# Create your tests here.
from rest_framework import status


class APITest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def badURL(self):
        request = self.factory.post('/api/webpage/data')
        self.assertTrue(request.status_code, 400)

