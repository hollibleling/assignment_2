from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from .models import Menu
from .serializers import MenuSerializer
from rest_framework import permissions

from .permissions import CustomAuthenticated
from .pagination import CustomPagination

class ProductViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset          = Menu.objects.all()
    serializer_class   = MenuSerializer
    permission_classes = [permissions.IsAuthenticated, CustomAuthenticated]
    pagination_class   = CustomPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.IsAuthenticated]

        return super().get_permissions()