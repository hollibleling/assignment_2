from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from .models import Menu, Item, Tag
from .serializers import MenuSerializer, ItemSerializer, TagSerializer
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

class ItemViewSet(CreateModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [CustomAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data.setdefault('menu', kwargs['product_pk'])
        return super().create(request, *args, **kwargs)


class TagViewSet(CreateModelMixin,
                 UpdateModelMixin,
                 DestroyModelMixin,
                 GenericViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [CustomAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data.setdefault('menu', kwargs['product_pk'])
        return super().create(request, *args, **kwargs)