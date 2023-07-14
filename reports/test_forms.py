from django.test import TestCase
from .models import Report, Comment
from django.contrib.auth.models import User
from .forms import CommentForm


class TestCommentForm(TestCase):

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
            content='This is a test comment',
            report=self.report,
        )

    def test_content_validation_with_valid_input(self):
        form = CommentForm(data={'content': 'This is a valid comment.'})
        self.assertTrue(form.is_valid())

    def test_form_validation_with_empty_content(self):
        form = CommentForm(data={'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)

    def test_form_save_functionality(self):
        form = CommentForm(data={'content': self.comment.content})
        self.assertTrue(form.is_valid())
        comment = form.save(commit=False)
        comment.report = self.report
        comment.save()

        self.assertIsInstance(comment, Comment)
        self.assertEqual(comment.content, self.comment.content)
        self.assertEqual(comment.report, self.report)
