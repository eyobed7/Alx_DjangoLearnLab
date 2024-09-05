from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to edit objects.
    Unauthenticated users have read-only access.
    """

    def has_permission(self, request, view):
        # Allow read-only access for unauthenticated users
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write access for authenticated users
        return request.user and request.user.is_authenticated
