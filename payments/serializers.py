from rest_framework import serializers
from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializer for Payment model.
    """
    class Meta:
        model = Payment
        fields = "__all__"
        read_only_fields = ["user", "status", "created_at"]

    def validate_amount(self, value):
        """
        Check if the payment amount is greater than zero.
        """
        if value <= 0:
            raise serializers.ValidationError("Payment amount must be greater than zero.")
        return value

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)
