from rest_framework import permissions


class IsReadOnly(permissions.BasePermission):
    """
    The request is a read-only.
    """
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
        )
