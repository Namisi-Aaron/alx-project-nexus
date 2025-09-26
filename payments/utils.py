import logging
import requests
from django.conf import settings

logger = logging.getLogger(__name__)

CHAPA_INIT_URL = f"{settings.CHAPA_API_BASE}/transaction/initialize"

def initialize_chapa_payment(amount, email, first_name, last_name, phone_number, tx_ref):
    """
    Initializes a Chapa payment transaction.

    Args:
        email (str): The email address of the customer.
        amount (float): The amount to be paid.
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        phone_number (str): The phone number of the customer.
        tx_ref (str): A unique reference for the transaction.

    Returns:
        dict: The response from the Chapa API.
    """
    headers = {
        "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "amount": str(amount),
        "currency": "ETB",
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "tx_ref": tx_ref,
        "callback_url": settings.CHAPA_CALLBACK_URL,
        "customization": {
            "title": "e_commerce app",
            "description": "I love Django"
        }
    }

    response = requests.post(CHAPA_INIT_URL, json=payload, headers=headers)
    try:
        return response.json()
    except Exception as e:
        logger.error(f"Error parsing Chapa response: {e}")
        return {"details": str(e)}
