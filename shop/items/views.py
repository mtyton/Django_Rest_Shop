from rest_framework import viewsets, filters
from .models import Category, Item
from .serializers import CategorySerialzier, ItemSerializer
from.pagination import newLimitOffsetPagination
from .permissions import IsAdminOrReadOnly


class CategoriesView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzier
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['pid']
    search_fields = ['name']
    pagination_class = newLimitOffsetPagination
    permission_classes = [IsAdminOrReadOnly]


class ItemsView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = newLimitOffsetPagination
    permission_classes = [IsAdminOrReadOnly]
