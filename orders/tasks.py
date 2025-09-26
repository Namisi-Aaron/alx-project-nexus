import logging
from celery import shared_task
from django.core.mail import send_mail
from orders.models import Order

logger = logging.getLogger(__name__)

@shared_task
def send_order_creation_email(order_id, user_email, user_name):
    """
    Task to send a notification email to users when a new order is created.

    Args:
        order_id (int): The ID of the order.
        user_email (str): The email address of the user.
        user_name (str): The name of the user.
    """
    try:
        order = Order.objects.get(id=order_id)
        subject = f"New Order: Order ID {order_id}"
        message = f"Hello {user_name},\n\nYou have created a new order with ID {order_id}.\n\nOrder to be shipped to {order.shipping_address}."
        from_email = "noreply@app.com"
        recipient_list = [user_email]

        send_mail(subject, message, from_email, recipient_list)

        logger.info(f"Notification email sent to {user_name} for order ID {order_id}.")
        return f"Notification email sent to {user_name} for order ID {order_id}."
    except Exception as e:
        logger.error(f"Error occurred while sending notification email for order ID {order_id}: {str(e)}")
        return f"details: {str(e)}"
