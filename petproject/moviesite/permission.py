from rest_framework import permissions


class CheckMovie(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
         if obj.status_cinema == 'pro' and request.user.status != 'pro':
            return False
         return True
