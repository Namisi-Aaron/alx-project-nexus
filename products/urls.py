from django.urls import path

from products.views import (
    # Product views
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductRetrieveUpdateDestroyAPIView,

    # Category views
    CategoryCreateView,
    CategoryListView,
    CategoryRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # Product URLs
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/update/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-update'),

    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
]