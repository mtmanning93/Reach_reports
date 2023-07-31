from allauth.account.auth_backends import AuthenticationBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailAuthenticationBackend(AuthenticationBackend):
    def authenticate(self, request, **credentials):
        email = credentials.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
                if user.check_password(credentials['password']):
                    return user
            except User.DoesNotExist:
                return None
        return None
