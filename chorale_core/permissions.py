from rest_framework import permissions


class SubscriberPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['OPTIONS', 'POST']:
            return True
        else:
            return permissions.IsAuthenticated.has_permission(self, request, view)
