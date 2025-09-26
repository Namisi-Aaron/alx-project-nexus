from django.db import models
from orders.models import Order
from users.models import CustomUser


class Payment(models.Model):
    """
    Model representing a payment made on an order.

    Fields:
    - order: Foreign key to the Order model.
    - user: Foreign key to the CustomUser model.
    - amount: Decimal field representing the payment amount.
    - status: Char field representing the payment status (pending, completed, failed).
    - created_at: DateTime field representing the creation date of the payment.
    """
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed")
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments")
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="payments"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for order {self.order.id} by {self.user.username}"
