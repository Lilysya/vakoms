from django.contrib.auth.backends import ModelBackend

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class MyAuth:
    def authenticate(request, email="", password=""):
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(request, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
