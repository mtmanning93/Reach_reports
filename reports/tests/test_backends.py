from django.test import TestCase
from django.contrib.auth import get_user_model
from allauth.account.auth_backends import AuthenticationBackend

from reports.backends import EmailAuthenticationBackend

User = get_user_model()


class EmailAuthenticationBackendTest(TestCase):

    def setUp(self):

        self.backend = EmailAuthenticationBackend()

        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword')

    def test_authenticate_with_valid_credentials(self):

        credentials = {
            'email': 'test@example.com',
            'password': 'testpassword'

            }

        authenticated_user = self.backend.authenticate(
            request=None, **credentials
            )

        self.assertEqual(authenticated_user, self.user)

    def test_authenticate_with_invalid_email(self):
        # Test with invalid email
        credentials = {
            'email': 'nonexistent@example.com',
            'password': 'testpassword'
            }

        authenticated_user = self.backend.authenticate(
            request=None, **credentials
            )

        self.assertIsNone(authenticated_user)

    def test_authenticate_with_invalid_password(self):
        # Test invalid password
        credentials = {
            'email': 'test@example.com',
            'password': 'wrongpassword'
            }

        authenticated_user = self.backend.authenticate(
            request=None, **credentials
            )

        self.assertIsNone(authenticated_user)
