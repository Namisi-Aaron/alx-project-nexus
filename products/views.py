from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from products.models import Product, Category
from products.filters import ProductFilter, CategoryFilter
from products.serializers import ProductSerializer, CategorySerializer


# Product Views
class ProductCreateView(CreateAPIView):
    """
    API view for creating a new product.

    Allows only admin users to create a new product.

    Returns:
        Response: A JSON response with the created product data.
        status: 201 Created if the product is created successfully,
            else 500 Internal Server Error.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                product = serializer.save()
                if product:
                    return Response(serializer.data, status=201)
        except Exception as e:
            return Response({"details": str(e)}, status=500)


@method_decorator(cache_page(60 * 10), name="dispatch")
class ProductListView(ListAPIView):
    """
    API view for listing all products.

    Allows any user to retrieve a list of all products.

    Returns:
        Response: A JSON response with all product data.
        status: 200 OK if the products are retrieved successfully,
            else 500 Internal Server Error.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    ordering_fields = ['name']
    permission_classes = [AllowAny]


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a product.

    Allows only admin users to update or delete products.

    Returns:
        Response: A JSON response with the updated or deleted product data.
        status: 200 OK if the product is retrieved, updated,
            or deleted successfully, else 500 Internal Server Error.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ProductDetailView(RetrieveAPIView):
    """
    API view for retrieving a product.

    Allows any user to retrieve a product.

    Returns:
        Response: A JSON response with the product data.
        status: 200 OK if the product is retrieved successfully,
            else 500 Internal Server Error.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


# Category Views
class CategoryCreateView(CreateAPIView):
    """
    API view for creating a new category.

    Allows only admin users to create categories.

    Returns:
        Response: A JSON response with the created category data.
        status: 201 Created if the category is created successfully,
            else 500 Internal Server Error.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                category = serializer.save()
                if category:
                    return Response(serializer.data, status=201)
        except Exception as e:
            return Response({"details": str(e)}, status=500)


@method_decorator(cache_page(60 * 10), name="dispatch")
class CategoryListView(ListAPIView):
    """
    API view for listing all categories.

    Allows access to all users.

    Returns:
        Response: A JSON response with all category data.
        status: 200 OK if the categories are retrieved successfully,
            else 500 Internal Server Error.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    ordering_fields = ['name']
    permission_classes = [AllowAny]


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a category.
    
    Allows access to admin users only.

    Returns:
        Response: A JSON response with the updated or deleted category data.
        status: 200 OK if the category is retrieved, updated,
            or deleted successfully, else 500 Internal Server Error.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
