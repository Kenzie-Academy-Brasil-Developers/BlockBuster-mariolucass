from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class AuthenticatedPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_authenticated


class EmployeeOrOwnerPermissions(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User):
        return request.user.is_superuser or user.email == request.user.email


class EmployeeOrReadOnlyPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.method in permissions.SAFE_METHODS or request.user.is_authenticated and request.user.is_superuser
