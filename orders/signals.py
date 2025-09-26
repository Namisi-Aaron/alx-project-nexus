from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from orders.models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_order_total(sender, instance, created, **kwargs):
    """
    Updates the total amount of an order
    when an order item is created or updated.
    """
    if created:
        order = instance.order
        order.total_amount += instance.subtotal
        order.save()


@receiver(post_delete, sender=OrderItem)
def update_order_total_delete(sender, instance, **kwargs):
    """
    Updates the total amount of an order
    when an order item is deleted.
    """
    order = instance.order
    order.total_amount -= instance.subtotal
    order.save()
