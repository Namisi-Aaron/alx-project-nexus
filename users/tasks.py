import logging
from celery import shared_task
from django.core.mail import send_mail

logger = logging.getLogger(__name__)

@shared_task
def send_user_creation_email(user_email, username):
    """
    Task to send a welcome email to a new user.

    Args:
        user_email (str): The email address of the user.
        username (str): The username of the user.
    """
    try:
        subject = "Welcome to E-Commerce (ALX-Project-Nexus)!"
        message = f"Welcome {username},\n\nYour account has been created successfully."
        from_email = "noreply@app.com"
        recipient_list = [user_email]

        send_mail(subject, message, from_email, recipient_list)

        logger.info(f"Email sent to {user_email}.")
        return f"Email sent to {user_email}."
    except Exception as e:
        logger.error(f"Error occurred while sending email to {user_email}: {str(e)}")
        return f"details: {str(e)}"
