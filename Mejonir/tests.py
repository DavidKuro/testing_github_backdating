from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.
class Tests(TestCase):
    def index(self):
        response=self.client.get('index')
        self.assertEqual(response.status_code,200)
