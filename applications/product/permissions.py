from rest_framework import permissions

class IsSuperuserOrReadOnly(permissions.BasePermission):
    """
    Allow access only to superusers for write operations (update, delete),
    for all other users read-only access is granted.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser

class IsSuperuser(permissions.BasePermission):
    """
    Allow access only to superusers.
    """
    def has_permission(self, request, view):
        return request.user.is_superuser
