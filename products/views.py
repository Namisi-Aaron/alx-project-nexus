from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer

# Product Views
class ProductCreateView(CreateAPIView):
    """
    API view for creating a new product.
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

class ProductListView(ListAPIView):
    """
    API view for listing all products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class ProductDetailView(RetrieveAPIView):
    """
    API view for retrieving a product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

# Category Views

class CategoryCreateView(CreateAPIView):
    """
    API view for creating a new category.
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

class CategoryListView(ListAPIView):
    """
    API view for listing all categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
