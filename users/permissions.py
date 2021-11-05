from rest_framework.permissions import BasePermission
from users.models import User


class CustomAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.ADMIN
