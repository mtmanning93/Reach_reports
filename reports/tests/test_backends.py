from django.test import TestCase
from django.contrib.auth.models import User
from allauth.account.auth_backends import AuthenticationBackend

from reports.backends import EmailAuthenticationBackend


class EmailAuthenticationBackendTest(TestCase):
    """
    Unit tests for the EmailAuthenticationBackend class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """

        self.backend = EmailAuthenticationBackend()

        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword')

    def test_authenticate_with_valid_credentials(self):
        """
        Ensures that a user can be successfully authenticated using valid
        email and password credentials.
        """

        credentials = {
            'email': 'test@example.com',
            'password': 'testpassword'

            }

        authenticated_user = self.backend.authenticate(
            request=None, **credentials
            )

        self.assertEqual(authenticated_user, self.user)

    def test_authenticate_with_invalid_email(self):
        """
        Tests user cant be authenticated with an invalid email.
        """
        credentials = {
            'email': 'nonexistent@example.com',
            'password': 'testpassword'
            }

        authenticated_user = self.backend.authenticate(
            request=None, **credentials
            )

        self.assertIsNone(authenticated_user)

    def test_authenticate_with_invalid_password(self):
        """
        Tests user cant be authenticated with an invalid password.
        """
        credentials = {
            'email': 'test@example.com',
            'password': 'wrongpassword'
            }

        authenticated_user = self.backend.authenticate(
            request=None, **credentials
            )

        self.assertIsNone(authenticated_user)
