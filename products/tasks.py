from celery import shared_task
from django.core.mail import send_mail
from products.models import Product

@shared_task
def send_low_stock_alert(product_id):
    """
    Task to send an email notification when a product's stock falls below 10.

    Args:
        product_id (int): The ID of the product.
    """
    try:
        product = Product.objects.get(id=product_id)
        if product.stock <= 10:
            subject = f"Low stock alert: {product.name}"
            message = f"The stock of {product.name} is running low.\n\n"
            message += f"{product.stock} units left."
            from_email = "noreply@app.com"
            recipient_list = ["admin@example.com"]

            send_mail(subject, message, from_email, recipient_list)
            return f"Low stock alert email sent for product ID {product_id}."
    except Exception as e:
        return f"Error occurred while sending low stock alert: {str(e)}"
