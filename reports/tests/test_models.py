from django.test import TestCase
from django.contrib.auth.models import User
from reports.models import Report, Comment


class TestModels(TestCase):

    def setUp(self):

        self.user = User.objects.create(username="testuser")

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

        self.comment = Comment.objects.create(
            report=self.report,
            name="Tester",
            email="testing@example.com",
            content="Test Comment",
            approved=True
        )

    def test_report_status_defaults_to_published(self):
        self.assertTrue(self.report.status)

    def test_report_string_method_returns_title(self):
        self.assertEqual(str(self.report), self.report.title)

    def test_report_number_of_likes(self):

        self.assertEqual(self.report.number_of_likes(), 0)
        self.report.likes.add(self.user)
        self.assertEqual(self.report.number_of_likes(), 1)

    def test_comment_approved_defaults_to_true(self):

        self.assertTrue(self.comment.approved)

    def test_comment_string_method_returns_correctly(self):

        self.assertEqual(
            str(self.comment),
            f"Comment {self.comment.content} by {self.comment.name}"
            )
