from django.utils.functional import SimpleLazyObject
from django.conf import settings
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.contrib import auth
from django.contrib.auth.models import AnonymousUser
from accounts.models import Token


def token_get_user(request):
    """
    Return the user model instance associated with the given request session.
    If no user is retrieved, return an instance of `AnonymousUser`.
    """
    user = None
    authorization = request.META.get("HTTP_AUTHORIZATION", None)
    if authorization:
        auth_type, key = authorization.split()
        if auth_type == "Token":
            token = Token.objects.select_related('user').get(key=key)
            user = token.user
    return user or AnonymousUser()


def get_user(request):
    if not hasattr(request, '_cached_user'):
        user = auth.get_user(request)
        if user == AnonymousUser():
            user = token_get_user(request)
        request._cached_user = user
    return request._cached_user


class AuthTokenMiddleware(AuthenticationMiddleware):
    def process_request(self, request):
        assert hasattr(request, 'session'), (
            "The Django authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE%s setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'django.contrib.auth.middleware.AuthenticationMiddleware'."
        ) % ("_CLASSES" if settings.MIDDLEWARE is None else "")
        request.user = SimpleLazyObject(lambda: get_user(request))
