from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin

