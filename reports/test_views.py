from django.test import TestCase
from .models import Report


class TestReportsView(TestCase):

    def test_get_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # def test_report_details(self):
