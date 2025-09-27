import logging
from celery import shared_task
from django.core.mail import send_mail
from payments.models import Payment

logger = logging.getLogger(__name__)

@shared_task
def send_payment_completion_email(payment_id, user_email, user_name, status):
    """
    Task to send an email notification to users when a payment is completed.

    Args:
        payment_id (int): The ID of the payment.
        user_email (str): The email address of the user.
        user_name (str): The name of the user.
    """
    try:
        payment = Payment.objects.get(id=payment_id)
        order = payment.order

        if status == "completed":
            subject = "Payment Completed"
            message = f"Hello {user_name},\n\nYour payment for order ID {order} has been completed."
            message += f"\n\nOrder details:\nOrder ID: {order.id}\nTotal amount: {order.total_amount}\nShipping address: {order.shipping_address}"
            from_email = "noreply@app.com"
            recipient_list = [user_email]
        else:
            subject = "Payment Failed"
            message = f"Hello {user_name},\n\nYour payment for order ID {order} has failed."
            message += f"\n\nOrder details:\nOrder ID: {order.id}\nTotal amount: {order.total_amount}\nShipping address: {order.shipping_address}"
            from_email = "noreply@app.com"
            recipient_list = [user_email]
        
        send_mail(subject, message, from_email, recipient_list)

        logger.info(f"Payment completion email sent to {user_name} for payment ID {payment_id}.")
        return f"Payment completion email sent to {user_name} for payment ID {payment_id}."
    except Exception as e:
        logger.error(f"Error occurred while sending payment completion email for payment ID {payment_id}: {str(e)}")
        return f"details: {str(e)}"
