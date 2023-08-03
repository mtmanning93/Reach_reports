from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.shortcuts import reverse
from reports.models import Report, Comment, ImageFile
from reports.forms import CreateReportForm, UpdateAccountForm
from django.core.files.uploadedfile import SimpleUploadedFile
from reports.views import generate_slug, validate_report_creation, validate_edit_report_image_data


class TestViews(TestCase):
    # SET UP
    def setUp(self):

        self.user = User.objects.create(
            username="testuser",
            email='test@example.com',
            password='testpassword'
        )

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

    def test_get_correct_report_details(self):
        url = reverse('report_details', args=[self.report.pk])
        expected_url = f'/reports/report/{self.report.pk}/'
        self.assertEqual(url, expected_url)

    def test_get_report_comments(self):
        Comment.objects.create(report=self.report, content="Test comment")
        response = self.client.get(
            reverse('report_details', args=[self.report.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test comment')
        comments = response.context['comments']
        self.assertEqual(comments.count(), 1)
        comment_report = comments.first().report
        self.assertEqual(comment_report, self.report)

    def test_get_account_page(self):
        self.client.force_login(self.user)
        response = self.client.get('/reports/account/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')

    def test_get_correct_user_account(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('account'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.email)
        self.assertContains(response, self.report.title)


class ReportListViewTests(TestCase):
    def setUp(self):

        self.user = User.objects.create(
            username="testuser",
            email='test@example.com',
            password='testpassword'
        )

        # Create sample reports for testing
        Report.objects.create(
            title="Report 1",
            author=self.user,
            status=1,
            overall_conditions="good",
            activity_category="alpine",
            start_date="2023-07-09",
            end_date="2023-07-10",
        )
        Report.objects.create(
            title="Report 2",
            author=self.user,
            status=1,
            overall_conditions="ok",
            activity_category="hike",
            start_date="2023-07-09",
            end_date="2023-07-10",
        )
        Report.objects.create(
            title="Report 3",
            author=self.user,
            status=1,
            overall_conditions="perfect",
            activity_category="ski",
            start_date="2023-07-09",
            end_date="2023-07-10",
        )

    def test_filter_by_activity_and_grade(self):
        url = reverse('reports') + '?activity=alpine&grade=good'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        reports = response.context['object_list']
        self.assertEqual(reports.count(), 1)
        self.assertEqual(reports[0].title, 'Report 1')

    def test_filter_by_activity_only(self):
        url = reverse('reports') + '?activity=hike'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        reports = response.context['object_list']
        self.assertEqual(reports.count(), 1)
        self.assertEqual(reports[0].title, 'Report 2')

    def test_filter_by_grade_only(self):
        url = reverse('reports') + '?grade=perfect'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        reports = response.context['object_list']
        self.assertEqual(reports.count(), 1)
        self.assertEqual(reports[0].title, 'Report 3')

    def test_filter_all_activities_and_grades(self):
        url = reverse('reports') + '?activity=all&grade=all'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        reports = response.context['object_list']
        self.assertEqual(reports.count(), 3)


class LikeReportTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create(
            username="testuser",
            email='test@example.com',
            password='testpassword'
        )

        # Create a test report
        self.report = Report.objects.create(
            title="Tester",
            author=self.user,
            status=1,
            overall_conditions="perfect",
            activity_category="ski",
            start_date="2023-07-09",
            end_date="2023-07-10",
        )

    def test_like_report(self):
        # Simulate an authenticated user
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('like_report', kwargs={'pk': self.report.pk}))

        self.assertRedirects(
            response, reverse('report_details', kwargs={'pk': self.report.pk}))
        self.assertTrue(self.report.likes.filter(id=self.user.id).exists())

    def test_unlike_report(self):
        # like the report
        self.client.force_login(self.user)
        self.client.post(reverse('like_report', kwargs={'pk': self.report.pk}))
        # unlike
        response = self.client.post(
            reverse('like_report', kwargs={'pk': self.report.pk}))

        self.assertRedirects(
            response, reverse('report_details', kwargs={'pk': self.report.pk}))
        self.assertFalse(self.report.likes.filter(id=self.user.id).exists())


class DeleteCommentTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
            )

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

        # Create a test comment
        self.comment = Comment.objects.create(
            name='testuser',
            content='Test comment content.',
            report=self.report
        )

    def test_delete_comment(self):
        self.client.login(username='testuser', password='testpassword')
        delete_url = reverse('delete_comment', args=[self.comment.pk])
        response = self.client.post(delete_url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())


class CreateReportTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )

        self.login_status = self.client.login(
            username='testuser', password='testpassword'
        )

    def test_create_report_view_GET(self):
        response = self.client.get(reverse('create_report'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_report.html')
        self.assertContains(response, '<form')
        self.assertIsInstance(
            response.context['report_form'], CreateReportForm)

    def test_create_report_view_with_valid_form(self):
        # Ensure the view creates a report on valid POST request
        report_data = {
            'title': 'Test Report',
            'start_date': '2023-07-29',
            'end_date': '2023-07-30',
            'goal_reached': 'yes',
            'height_in_meters': 3500,
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'This is a test report.',
            'number_in_group': 3,
            'number_on_route': 2,
            'status': 1,
            'images': [open('reports/tests/test_img.png', 'rb')],
        }
        response = self.client.post(
            reverse('create_report'), data=report_data, follow=True)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Report.objects.count(), 1)
        self.assertEqual(ImageFile.objects.count(), 1)

        self.assertTemplateUsed(response, 'reports.html')
        self.assertContains(response, 'Report created successfully!')
        self.assertTrue(Report.objects.filter(title='Test Report').exists())

        image = ImageFile.objects.first()
        self.assertTrue(
            image.image_file.url.startswith(
                'https://res.cloudinary.com/dsmfunyxk/image/upload/'))

    def test_create_report_view_with_invalid_form(self):
        report_data = {}  # Empty to create invalid input
        response = self.client.post(reverse('create_report'), data=report_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_report.html')
        self.assertContains(response, 'is-invalid')
        self.assertFalse(Report.objects.filter(title='Test Report').exists())


class ValidateReportCreationTests(TestCase):

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

        self.test_image = ImageFile.objects.create(
            report=self.report, image_file='test_image1.jpg')

    def test_validate_report_with_under_12_images(self):

        form_data = {
            'title': 'Updated Test Report',
            'slug': 'sample-report',
            'author': 'Tester',
            'start_date': '2023-07-13',
            'end_date': '2023-07-15',
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Updated content.',
            'goal_reached': 'yes',
            'number_in_group': 3,
            'number_on_route': 2,
            'status': 1,
        }

        # Mock 10 image files
        images = [self.test_image for _ in range(10)]

        form = CreateReportForm(data=form_data)
        form.is_valid()  # Validate the form
        result = validate_report_creation(images, form)

        # More than 12 images (validator function = True)
        self.assertTrue(result)

    def test_validate_report_with_over_12_images(self):

        form_data = {
            'title': 'Updated Test Report',
            'slug': 'sample-report',
            'author': 'Tester',
            'start_date': '2023-07-13',
            'end_date': '2023-07-15',
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Updated content.',
            'goal_reached': 'yes',
            'number_in_group': 3,
            'number_on_route': 2,
            'status': 1,
        }

        # Mock 15 image files
        images = [self.test_image for _ in range(15)]  

        form = CreateReportForm(data=form_data)
        form.is_valid()  # Validate the form
        result = validate_report_creation(images, form)

        # More than 12 images (validator function = False)
        self.assertFalse(result)

        # Check if there errors
        self.assertIn(
            '__all__', form.errors)  
        # Check if there's one error message
        self.assertEqual(
            len(form.errors['__all__']), 1)
        # Check first index is the correct error
        self.assertEqual(
            form.errors['__all__'][0],
            "Invalid Input: You can upload a maximum of 12 images."
            )


class GenerateSlugTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create(username="testuser")

    def test_generate_slug_unique(self):
        # Create two reports with the same title and author
        report1 = Report.objects.create(
            title="Sample Report",
            author=self.user,
            start_date="2023-07-13",
            end_date="2023-07-15",
            overall_conditions="Good",
            activity_category="Hiking",
            description="This is a sample report."
        )
        report2 = Report.objects.create(
            title="Sample Report",
            author=self.user,
            start_date="2023-07-13",
            end_date="2023-07-15",
            overall_conditions="Good",
            activity_category="Hiking",
            description="This is another sample report."
        )
        self.assertNotEqual(report1.slug, report2.slug)


class EditReportTests(TestCase):

    def setUp(self):

        self.client = Client()

        self.user = User.objects.create(
            username="testuser",
            email='test@example.com',
            password='testpassword'
        )

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

        self.image1 = ImageFile.objects.create(
            report=self.report, image_file='test_image1.jpg')
        self.image2 = ImageFile.objects.create(
            report=self.report, image_file='test_image2.jpg')
        self.image1_pk = ImageFile.pk

    def test_edit_report_view_with_new_images(self):

        self.client.force_login(self.user)
        # Prepare the data for the test
        form_data = {
            'title': 'Updated Test Report',
            'slug': 'sample-report',
            'author': 'Tester',
            'start_date': '2023-07-13',
            'end_date': '2023-07-15',
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Updated content.',
            'goal_reached': 'yes',
            'number_in_group': 3,
            'number_on_route': 2,
            'status': 1,
        }
        new_image_file = ImageFile.objects.create(
            report=self.report, image_file='test_image3.jpg')

        # Post the edit_report form data and new image
        response = self.client.post(
            reverse('edit_report', args=[self.report.pk]),
            form_data,
            format='multipart',
            FILES={'images': [new_image_file]}, follow=True)
        # Check image files are added
        # print(ImageFile.objects.filter(report=self.report))
        self.assertEqual(
            ImageFile.objects.filter(report=self.report).count(), 3)

        # Check that image file exists with the correct report and name
        image_exists = ImageFile.objects.filter(
            report=self.report, image_file='test_image3.jpg').exists()
        self.assertTrue(image_exists)

    def test_edit_report_view_GET(self):
        report = self.report
        response = self.client.get(reverse('edit_report', args=[report.pk]))
        self.assertEqual(response.status_code, 200)

    def test_confirm_deletion_false(self):
        form_data = {
            'confirm-deletion': 'false',
            # No image
        }
        response = self.client.post(reverse(
            'edit_report', args=[self.report.pk]), data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check if the image is still present in the database and Cloudinary
        images_present = ImageFile.objects.filter(report=self.report).exists()
        self.assertTrue(images_present)

    def test_confirm_deletion_true(self):
        form_data = {
            'confirm-deletion': 'true',
            f'delete_image_{self.image1.pk}': 'on',
        }
        response = self.client.post(reverse(
            'edit_report', args=[self.report.pk]), data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check if the image is deleted from the database and Cloudinary
        images_deleted = ImageFile.objects.filter(report=self.report).exists()
        self.assertTrue(images_deleted)


class ValidateEditReportImageDataTests(TestCase):

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

        self.test_image = ImageFile.objects.create(
            report=self.report, image_file='test_image1.jpg')

    def test_edit_report_images_valid_data(self):

        form_data = {
            'title': 'Updated Test Report',
            'slug': 'sample-report',
            'author': 'Tester',
            'start_date': '2023-07-13',
            'end_date': '2023-07-15',
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Updated content.',
            'goal_reached': 'yes',
            'number_in_group': 3,
            'number_on_route': 2,
            'status': 1,
        }
        # Must equal 12 or less
        new_images = [self.test_image for _ in range(5)]
        curr_images = [self.test_image for _ in range(4)]
        delete_these = [self.test_image for _ in range(3)]

        form = CreateReportForm(data=form_data)
        form.is_valid()  # Validate the form
        result = validate_edit_report_image_data(
            new_images, curr_images, delete_these, form)

        self.assertTrue(result)

    def test_edit_report_images_invalid_data(self):

        form_data = {
            'title': 'Updated Test Report',
            'slug': 'sample-report',
            'author': 'Tester',
            'start_date': '2023-07-13',
            'end_date': '2023-07-15',
            'overall_conditions': 'good',
            'activity_category': 'hike',
            'description': 'Updated content.',
            'goal_reached': 'yes',
            'number_in_group': 3,
            'number_on_route': 2,
            'status': 1,
        }

        # Total should be 15 (new + curr - delete)
        new_images = [self.test_image for _ in range(4)]
        curr_images = [self.test_image for _ in range(12)]
        delete_these = [self.test_image for _ in range(3)]

        form = CreateReportForm(data=form_data)
        form.is_valid()
        result = validate_edit_report_image_data(
            new_images, curr_images, delete_these, form)

        self.assertFalse(result)


class DeleteReportTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )

        self.report = Report.objects.create(
            title='Sample Report',
            start_date='2023-07-27',
            end_date='2023-07-28',
            author=self.user,
        )

    def test_delete_report_deletes_report(self):
        self.client.login(
            username=self.user.username, password=self.user.password
            )
        response = self.client.post(reverse('delete', args=[self.report.pk]))
        # Check if the report is deleted and redirects
        self.assertEqual(response.status_code, 302)  # Redirect not success
        # Check if the report is deleted in db
        report_exists = Report.objects.filter(pk=self.report.pk).exists()
        self.assertFalse(report_exists)


class DeleteAccountTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
        )

        self.client.login(username='testuser', password='testpassword')

    def test_delete_account_deletes_account_and_redirects(self):

        response = self.client.post(reverse('delete_account'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='testuser').exists())

    def test_delete_account_redirects_to_account_not_delete(self):

        response = self.client.get(reverse('delete_account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')
        self.assertTrue(User.objects.filter(username='testuser').exists())


class UpdateAccountViewTests(TestCase):

    def setUp(self):

        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.login(
            username='testuser', password='testpassword'
        )
        self.url = reverse('update_account')

    def test_update_account_view_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_account.html')
        self.assertIn('form', response.context)

    def test_update_account_view_valid_form(self):

        new_data = {
            'username': 'new_username',
            'email': 'new_email@example.com',
        }

        response = self.client.post(self.url, data=new_data, follow=True)
        self.assertRedirects(response, reverse('account'))
        self.assertEqual(response.status_code, 200)

    def test_update_account_view_invalid_form(self):

        invalid_data = {
            'username': '',
            'email': 'new_email@example.com',
        }

        response = self.client.post(self.url, data=invalid_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, 'form', 'username', 'This field is required.')
