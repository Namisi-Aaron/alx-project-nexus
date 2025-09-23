from rest_framework import serializers
from products.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.
    """
    class Meta:
        """
        Meta options for ProductSerializer.
        """
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model.
    """
    class Meta:
        """
        Meta options for CategorySerializer.
        """
        model = Category
        fields = '__all__'
