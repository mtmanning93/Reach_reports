from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Report, Comment


class TestViews(TestCase):
    # SET UP
    def setUp(self):
        # Create a User instance
        self.user = User.objects.create(username="testuser")

        # Create a Report instance
        self.report = Report.objects.create(
            title="Sample Report",
            slug="sample-report",
            author=self.user,
            start_date="2023-07-13",
            end_date="2023-07-15",
            overall_conditions="Good",
            activity_category="Hiking",
            description="This is a sample report."
        )

    def test_get_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_reports_list_page(self):
        response = self.client.get('/reports/reports/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports.html')

    def test_get_report_details_page(self):
        response = self.client.get(f'/reports/report/{self.report.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report_details.html')

    # Test correct report details selected
    def test_get_correct_report_details(self):
        url = reverse('report_details', args=[self.report.pk])
        expected_url = f'/reports/report/{self.report.pk}/'
        self.assertEqual(url, expected_url)

    def test_get_report_comments(self):

        # Create a comment for the report
        Comment.objects.create(report=self.report, content="Test comment")

        response = self.client.get(
            reverse('report_details', args=[self.report.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test comment')

        # Test correct comment for correct report
        # Retrieve the comment from the response context
        comments = response.context['comments']
        self.assertEqual(comments.count(), 1)

        # Assert that the comment's report matches the expected report
        comment_report = comments.first().report
        self.assertEqual(comment_report, self.report)
