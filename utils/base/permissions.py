from rest_framework.permissions import BasePermission


class IsUserActive(BasePermission):
    """
    Allows access only to authenticated users.
    """
    message = 'Your account has been disabled.'

    def has_permission(self, request, view):
        return request.user.is_active
