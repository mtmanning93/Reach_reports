from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Report, Comment

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

    def test_form_saves_correctly(self):
        form = CommentForm(data={'content': self.comment.content})
        self.assertTrue(form.is_valid())
        comment = form.save(commit=False)
        comment.report = self.report
        comment.save()

        self.assertIsInstance(comment, Comment)
        self.assertEqual(comment.content, self.comment.content)
        self.assertEqual(comment.report, self.report)

    def test_comment_form_renders_correctly(self):
        form = CommentForm()
        self.assertIn('content', form.as_p())

    def test_comment_posts_to_page(self):

        client = Client()
        form_data = {
            'content': 'This is a test comment',
        }
        form = CommentForm(data=form_data)

        response = client.post(
            reverse(
                'report_details', kwargs={'pk': self.report.pk}
            ), data=form_data, follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, form_data['content'])
        saved_comments = Comment.objects.filter(content=form_data['content'])
        self.assertGreaterEqual(saved_comments.count(), 1)
        self.assertTrue(
            any(comment.report == self.report for comment in saved_comments)
        )

    
