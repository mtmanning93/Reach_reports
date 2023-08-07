from allauth.account.auth_backends import AuthenticationBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailAuthenticationBackend(AuthenticationBackend):

    def authenticate(self, request, **credentials):
        """
        Authenticate a user based on the provided email and password.
        Overridess the standard username authentication.
        Returns the authenticated user if the email and password are valid,
        None otherwise.
        """
        email = credentials.get('email')

        if email:
            try:
                user = User.objects.get(email=email)
                if user.check_password(credentials['password']):
                    return user

            except User.DoesNotExist:
                return None

        return None
