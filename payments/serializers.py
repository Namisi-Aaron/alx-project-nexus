from rest_framework import serializers
from users.serializers import CustomUserSerializer
from payments.models import Payment
from orders.models import Order


class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializer for Payment model.
    """
    user = CustomUserSerializer(read_only=True)
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = Payment
        fields = "__all__"
        read_only_fields = ["user", "status", "created_at"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")

        if request and not request.user.is_superuser:
            self.fields["order"].queryset = Order.objects.filter(user=request.user)
    
    
    def validate_amount(self, value):
        """
        Check if the payment amount is greater than zero.
        """
        if value <= 0:
            raise serializers.ValidationError("Payment amount must be greater than zero.")
        return value

    def validate_order(self, order):
        """
        Ensure non-admins cannot set someone else's order.
        """
        request = self.context.get("request")
        if request and not request.user.is_superuser and order.user != request.user:
            raise serializers.ValidationError("You may only create payments for your own orders.")
        return order

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)
