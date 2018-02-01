from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class TokenAuthBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        f = request
        return request