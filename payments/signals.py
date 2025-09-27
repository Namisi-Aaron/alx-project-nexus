from django.db.models.signals import post_save
from django.dispatch import receiver
from payments.models import Payment

@receiver(post_save, sender=Payment)
def update_order_status_on_payment(sender, instance, created, **kwargs):
    """
    Signal receiver for updating the order status when a payment is completed.

    Args:
        sender (Model): The model class that the signal is sent from.
        instance (Payment): The payment instance that was created.
    """
    order = instance.order

    if instance.status == "completed":
        if order.status != "shipped":
            order.status = "shipped"
            order.save(update_fields=["status"])
