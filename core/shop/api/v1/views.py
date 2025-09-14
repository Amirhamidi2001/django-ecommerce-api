from rest_framework import viewsets, filters, permissions
from shop.models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer
from .paginations import CustomPagination


class BrandViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Brand objects with search, ordering, and slug lookup.
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at"]
    ordering = ["name"]
    lookup_field = "slug"


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Category objects with search, ordering, and slug lookup.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at"]
    ordering = ["name"]
    lookup_field = "slug"


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Product objects with search, ordering, slug lookup, and pagination.
    """

    queryset = Product.objects.select_related("category", "brand").all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "description", "category__name", "brand__name"]
    ordering_fields = ["name", "price", "created_at"]
    ordering = ["name"]
    lookup_field = "slug"
    pagination_class = CustomPagination
