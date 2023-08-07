from django.test import Client, TestCase
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

from reports.models import Report, Comment
from reports.forms import CommentForm, CreateReportForm, UpdateAccountForm
from reports.views import generate_slug


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

        form_data = {
            'content': 'This is a test comment',
        }
        form = CommentForm(data=form_data)

        response = self.client.post(
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


class CreateReportFormTests(TestCase):

    def setUp(self):

        self.user = User.objects.create(username="testuser")

    def test_create_report_form_with_valid_data(self):

        form_data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date.today(),
            'end_date': date.today(),
            'height_in_meters': 3000,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'This is a test.',
            'number_in_group': 5,
            'number_on_route': 3,
            'gps_map_link': 'https://example.com/gps',
            'status': 1,
        }

        form = CreateReportForm(data=form_data)

        self.assertTrue(form.is_valid())

        report = form.save(commit=False)
        report.author = self.user
        report.save()

        saved_report = Report.objects.get(pk=report.pk)

        self.assertEqual(saved_report.title, form_data['title'])

    def test_create_report_form_with_missing_required_fields(self):

        form_data = {
            'start_date': str(date.today()),
            'end_date': str(date.today()),
            'goal_reached': 'yes',
            'height_in_meters': 2000,
            'overall_conditions': 'good',
            'activity_category': 'alpine',
        }

        form = CreateReportForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_create_report_form_with_invalid_data(self):

        form_data = {
            'title': 'Test Report Title',
            'goal_reached': 'invalid_choice',
            'start_date': date.today(),
            'end_date': 'invalid_date',
            'overall_conditions': 'invalid_choice',
            'activity_category': 'invalid_choice',
            'description': '',
            'number_in_group': 0,
            'number_on_route': 10,
            'gps_map_link': 'invalid_url',
            'status': 5,
        }

        form = CreateReportForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_create_report_form_with_optional_gps_map_link(self):

        form_data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date.today(),
            'end_date': date.today(),
            'height_in_meters': 3000,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'This is a test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'gps_map_link': '',
            'status': 1,
        }

        form = CreateReportForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_end_date_validaion(self):

        form_data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 7, 31),
            'height_in_meters': 3000,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'This is a test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
        }

        form = CreateReportForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('end_date', form.errors)
        self.assertEqual(
            form.errors['end_date'][0], "End date cannot be before start date."
            )


class TestTitleValidation(TestCase):

    def test_valid_title(self):
        # Test with a valid title
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'height_in_meters': 3000,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'This is a test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(data)
        self.assertTrue(form.is_valid())

    def test_title_too_short(self):
        # Test with a title that is too short
        form_data = data = {
            'title': 'A',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'height_in_meters': 3000,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'This is a test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            }

        form = CreateReportForm(form_data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            'Title must be between 3 and 30 characters.', form.errors['title'])

    def test_title_too_long(self):
        # Test with a title that is too long
        form_data = {
            'title': '''
                This is a very long title that exceeds the character limit''',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'height_in_meters': 3000,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'This is a test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(form_data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            'Title must be between 3 and 30 characters.', form.errors['title'])

    def test_title_contains_only_numbers(self):
        # Test with a title that contains only numbers
        form_data = {
            'title': '12345',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'height_in_meters': 3000,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'This is a test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Title cannot be just numbers.', form.errors['title'])

    def test_title_contains_numbers_and_letters(self):
        # Test with a title that contains both numbers and letters
        form_data = {
            'title': 'Title123',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'height_in_meters': 3000,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'This is a test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(form_data)
        self.assertTrue(form.is_valid())


class UpdateAccountFormTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_valid_form(self):

        initial_data = {
            'username': 'new_username',
            'email': 'new_email@example.com',
        }

        form = UpdateAccountForm(data=initial_data, instance=self.user)

        self.assertTrue(form.is_valid())

    def test_invalid_email(self):

        initial_data = {
            'username': 'new_username',
            'email': 'test_not_an_email',
        }

        form = UpdateAccountForm(data=initial_data, instance=self.user)

        self.assertFalse(form.is_valid())
        self.assertTrue('email' in form.errors)
