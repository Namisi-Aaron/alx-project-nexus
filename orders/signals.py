from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from orders.models import OrderItem, Order
from products.tasks import send_low_stock_alert


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

@receiver(post_save, sender=Order)
def reduce_inventory(sender, instance, created, **kwargs):
    """
    Reduces the inventory of products in an order
    when an order is created or updated.

    If the stock falls below 10, sends a low stock alert task.
    """
    if instance.status == "shipped":
        for item in instance.items.all():
            product = item.product
            product.stock -= item.quantity
            product.save()
            send_low_stock_alert.delay(product.id)
