from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'You can only edit your own profile'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsOwnerOrReadOnlyImages(permissions.BasePermission):
    message = 'You can only edit your own images'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.person.user == request.user
