from rest_framework.permissions import BasePermission


class IsOrderUser(BasePermission):
    def has_object_permission(self, request, views, obj):
        return obj.user == request.user
