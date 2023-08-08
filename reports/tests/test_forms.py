from django.test import Client, TestCase
from datetime import date, timedelta
from django.urls import reverse
from django.contrib.auth.models import User

from reports.models import Report, Comment
from reports.forms import CommentForm, CreateReportForm, UpdateAccountForm
from reports.views import generate_slug


class TestCommentForm(TestCase):
    """
    This test case covers the process of posting comments to a page using the
    CommentForm, and verifies that the posted comment content appears in the
    response.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
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

    def test_form_validation_with_valid_input(self):
        """
        Checks the comment form is submitted if content is valid
        """

        form = CommentForm(data={'content': 'This is a valid comment.'})

        self.assertTrue(form.is_valid())

    def test_form_validation_with_empty_content(self):
        """
        Test form validation when there is no input in the comment seciton
        Expected form validation error 'Please fill in this field.'
        """

        form = CommentForm(data={'content': ''})

        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)

    def test_form_saves_correctly(self):
        """
        Ensures that comments are associated with the correct report object
        when saved in the db.
        """

        form = CommentForm(data={'content': self.comment.content})

        self.assertTrue(form.is_valid())

        comment = form.save(commit=False)
        comment.report = self.report
        comment.save()

        self.assertIsInstance(comment, Comment)
        self.assertEqual(comment.content, self.comment.content)
        self.assertEqual(comment.report, self.report)

    def test_comment_form_renders_correctly(self):
        """
        Tests the correct fields are rendered within the CommentForm.
        'content' is the field which should be present in the rendered form.
        """

        form = CommentForm()

        self.assertIn('content', form.as_p())

    def test_comment_posts_to_page(self):
        """
        Ensures that when a comment is posted to a page using the CommentForm,
        the posted comment content appears in the response.
        """

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
    """
    This test case covers the process of validating and saving
    a report using the CreateReportForm with valid data.
    """
    def setUp(self):
        """
        Set up the test environment before each test method.
        """
        self.user = User.objects.create(username="testuser")

    def test_create_report_form_with_valid_data(self):
        """
        Checks that a report can be successfully validated and saved using
        valid data.
        """
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
        """
        Ensures the form is not valid if reuired fields are missing input.
        """
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
        """
        Tests that for is invalid with invalid data input.
        """
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
        """
        Ensures form s still valid with empty gps_map_link,
        meaning its an optional input for users!
        """
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
        """
        Tests that end_date is invalid if before start_date,
        and checks for correct error message.
        """

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
    """
    Test the title validator functionality.
    """
    def test_valid_title(self):
        """
        Checks the form is valid with a valid title input.
        """
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
        """
        Checks the correct validation error if the title is too short,
        and the error message is corresponding correctly.
        """
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
        """
        Checks the correct validation error if the title is too long,
        and the error message is corresponding correctly.
        """
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
        """
        Tests the title is not valid if it is only populated by numbers.
        """
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
        """
        Ensures a title is valid if it contains both numbers and letters.
        """
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


class TestStartDateValidation(TestCase):
    """
    Test the start_date validator functionality.
    """
    def test_valid_start_date(self):
        """
        Tests the form is valid when the start date is within the last 5 years.
        """
        five_years_ago = date.today() - timedelta(days=365*5)
        data = {
            'title': 'Title123',
            'goal_reached': 'yes',
            'start_date': five_years_ago,
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

    def test_start_date_in_future(self):
        """
        Checks the start date is invalid if it is in the future,
        and checks the corresponding error message is correct.
        """
        future_date = date.today() + timedelta(days=1)
        data = {
            'title': 'Title123',
            'goal_reached': 'yes',
            'start_date': future_date,
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

        self.assertFalse(form.is_valid())
        self.assertIn(
            'Start date cannot be in the future.', form.errors['start_date'])

    def test_start_date_more_than_5_years_ago(self):
        """
        Tests the start_date is not valid when more than 5 years old.
        """
        more_than_5_years_ago = date.today() - timedelta(
            days=365 * 6)
        data = {
            'title': 'Title123',
            'goal_reached': 'yes',
            'start_date': more_than_5_years_ago,
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

        self.assertFalse(form.is_valid())
        self.assertIn(
            """Start date must not be more than
                 5 years old, it keeps our reports current!""",
            form.errors['start_date'])


class TestEndDateValidation(TestCase):
    """
    Test the start_date validator functionality.
    """
    def test_valid_end_date(self):
        """
        Tests the form is valid when the end date is valid.
        """
        data = {
            'title': 'Title123',
            'goal_reached': 'yes',
            'start_date': date.today(),
            'end_date': date.today(),
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

    def test_end_date_before_start_date(self):
        """
        Tests to ensure end_date can not be before the start date,
        and checks the corresponding error message is correct.
        """
        start_date = date.today()
        end_date = start_date - timedelta(days=1)
        data = {
            'title': 'Title123',
            'goal_reached': 'yes',
            'start_date': start_date,
            'end_date': end_date,
            'height_in_meters': 3000,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'This is a test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "End date cannot be before start date.", form.errors['end_date'])

    def test_end_date_in_the_future(self):
        """
        Tests to ensure end_date can not be in the future,
        and checks the corresponding error message is correct.
        """
        future_date = date.today() + timedelta(days=1)
        data = {
            'title': 'Title123',
            'goal_reached': 'yes',
            'start_date': date.today(),
            'end_date': future_date,
            'height_in_meters': 3000,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'This is a test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "End date cannot be in the future.", form.errors['end_date'])


class TestTimeTakenValidation(TestCase):
    """
    Test the time_taken custom validator functionality.
    """
    def test_valid_time_format(self):
        """
        Tests a valid duration input.
        """
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
            'time_taken': '12:34:56'
            }
        form = CreateReportForm(data)

        self.assertTrue(form.is_valid())

    def test_empty_time_taken(self):
        """
        Tests the form is valid if the field is empty,
        or has no input.
        """
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
            'time_taken': ''
            }
        form = CreateReportForm(data)

        self.assertTrue(form.is_valid())

    def test_wrong_time_format(self):
        """
        Tests the time format used is correct (hh:mm:ss),
        otherwise it is invalid. Checks for the correct error message.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'height_in_meters': 3000,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            'time_taken': '200000'
            }
        form = CreateReportForm(data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "Invalid time format. Use hh:mm:ss.",
            form.errors['time_taken'])


class TestHeightInMetersValidation(TestCase):
    """
    Test the height_in_meters field custom validator functionality.
    """
    def test_valid_height(self):
        """
        Tests the form is valid with a valid height in meters input.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'height_in_meters': 3000,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(data)

        self.assertTrue(form.is_valid())

    def test_height_less_than_zero(self):
        """
        Test to check if the input is less than 0 the form is invalid.
        Checks the corresponding error message is correct.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'height_in_meters': -100,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "Ensure this value is greater than or equal to 0.",
            form.errors['height_in_meters'])

    def test_height_greater_than_everest(self):
        """
        Checks the height input isnt higher than the tallest possible
        climb, Mt. Everest at 8849m. Checks the correct error message
        is displayed.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'height_in_meters': 9000,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "Height must be less than 8850m (Everest).",
            form.errors['height_in_meters'])

    def test_height_is_none(self):
        """
        Tests to check that no input in this field still allows for
        valid form. Checks the field is optional.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'height_in_meters': None,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(data)

        self.assertTrue(form.is_valid())


class TestNumberInGroupValidation(TestCase):
    """
    Test case to check the number_in_group validator.
    """
    def test_valid_number(self):
        """
        Tests the field with a valid input.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(data)

        self.assertTrue(form.is_valid())

    def test_negative_number(self):
        """
        Tests the field with a negative number (-2).
        Checks tzhe correct error message is displayed.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': -2,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "Ensure this value is greater than or equal to 0.",
            form.errors['number_in_group'])

    def test_number_is_none(self):
        """
        Test to check if the input is 'None' (empty),
        the form is still valid.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': None,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(data)

        self.assertFalse(form.is_valid())


class TestNumberOnRouteValidation(TestCase):
    """
    Test case to check the number_on_route validator.
    """
    def test_valid_number(self):
        """
        Tests form with a valid number_on_route input.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': 5,
            'number_on_route': 3,
            'status': 1,
            }
        form = CreateReportForm(data)

        self.assertTrue(form.is_valid())

    def test_negative_number(self):
        """
        Checks the form with an invalid negative number input.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': 5,
            'number_on_route': -3,
            'status': 1,
            }
        form = CreateReportForm(data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "Ensure this value is greater than or equal to 0.",
            form.errors['number_on_route'])

    def test_number_is_none(self):
        """
        Tests with no input or 'None'. This is allowed.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': 5,
            'number_on_route': None,
            'status': 1,
            }
        form = CreateReportForm(data)

        self.assertFalse(form.is_valid())


class TestGPSMapLinkValidation(TestCase):
    """
    Test case to check the gps_map_link validator.
    """
    def test_valid_gps_map_link(self):
        """
        Checks the form is still valid with a valid gps_map_link input,
        Includes the 'fatmap.com' string.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': 3,
            'number_on_route': 3,
            'status': 1,
            'gps_map_link': 'https://www.fatmap.com/your-map'
            }
        form = CreateReportForm(data)

        self.assertTrue(form.is_valid())

    def test_invalid_gps_map_link(self):
        """
        Test with an invalid GPS map link not containing 'fatmap.com',
        but still a url. Checks the related error message is displayed.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': 3,
            'number_on_route': 3,
            'status': 1,
            'gps_map_link': 'https://www.google.com/maps'
            }
        form = CreateReportForm(data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "The GPS map link must be from fatmap.com.",
            form.errors['gps_map_link'])

    def test_gps_map_link_is_none(self):
        """
        Checks that no input still allows for a valid form.
        """
        data = {
            'title': 'Test Report Title',
            'goal_reached': 'yes',
            'start_date': date(2023, 8, 1),
            'end_date': date(2023, 8, 2),
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Test description.',
            'number_in_group': 3,
            'number_on_route': 3,
            'status': 1,
            'gps_map_link': None
            }
        form = CreateReportForm(data)

        self.assertTrue(form.is_valid())


class UpdateAccountFormTests(TestCase):
    """
    Test case to check UpdateAccountForm.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_valid_form(self):
        """
        Tests the form with valid inputs.
        """
        initial_data = {
            'username': 'new_username',
            'email': 'new_email@example.com',
        }

        form = UpdateAccountForm(data=initial_data, instance=self.user)

        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        """
        Test to check an invalid input in the email field.
        """
        initial_data = {
            'username': 'new_username',
            'email': 'test_not_an_email',
        }

        form = UpdateAccountForm(data=initial_data, instance=self.user)

        self.assertFalse(form.is_valid())
        self.assertTrue('email' in form.errors)
