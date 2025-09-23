from rest_framework.permissions import BasePermission


class IsSuperUserOrNotAuthenticated(BasePermission):
    """
    Allows access only if the user is not authenticated.
    """
    def has_permission(self, request, view):
        """"
        Check if the user is authenticated.

        Return True if the user is not authenticated or an admin.
        """
        return (
            not request.user.is_authenticated
        ) or request.user.is_superuser


class IsAdminOrSelf(BasePermission):
    """
    Allows access only if the user is authenticated
    and is either the user itself or an admin.
    """
    def has_permission(self, request, view):
        """
        Check if the user is authenticated
        and is either the user itself or an admin.

        Return True if the user is an admin
        or the user is the same as the requested user.
        """
        if request.user.is_superuser:
            return True
        return request.user.id == view.kwargs.get('pk', None)
