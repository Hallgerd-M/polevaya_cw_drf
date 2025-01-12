from rest_framework.permissions import BasePermission


class IsPublic(BasePermission):
    """Checks if habit is public"""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user or obj.public is True:
            return True
        return False
