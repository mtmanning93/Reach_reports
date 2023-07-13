from django.test import TestCase
from django.contrib.auth.models import User
from .models import Report, Comment


class TestModels(TestCase):
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

    def test_report_status_defaults_to_published(self):
        self.assertTrue(self.report.status)

    def test_comment_approved_defaults_to_true(self):
        # Create Comment Instance
        comment = Comment.objects.create(
            report=self.report,
            name="Tester",
            email="testing@example.com",
            content="Test Comment",
            approved=True
        )

        self.assertTrue(comment.approved)
