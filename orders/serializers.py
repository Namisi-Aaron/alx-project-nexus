from rest_framework import serializers
from orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for OrderItem model.
    """
    product_name = serializers.ReadOnlyField(source='product.name')
    subtotal = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'product_name',
            'quantity',
            'subtotal',
        ]


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order model.
    """
    user = serializers.CharField(source='user.username', read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    total_amount = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True,
    )

    class Meta:
        model = Order
        fields = [
            'user',
            'status',
            'shipping_address',
            'items',
            'total_amount',
            'created_at',
        ]
        read_only_fields = ['user', 'status', 'total_amount', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        order = Order.objects.create(**validated_data)
        return order
