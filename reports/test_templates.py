from django.test import TestCase
from django.urls import reverse
from .models import Report


class TestLandingPage(TestCase):

    def test_landing_page_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, 'index.html')


class TestReportsPage(TestCase):

    def test_reports_page_location(self):
        response = self.client.get('/reports/reports/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("reports"))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("reports"))
        self.assertTemplateUsed(response, 'reports.html')

    def test_template_content(self):
        response = self.client.get(reverse("reports"))
        self.assertContains(response, "<h1>Condition Reports</h1>")
        self.assertNotContains(response, "Not on the page")
