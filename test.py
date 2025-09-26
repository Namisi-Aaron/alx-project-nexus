import uuid
import requests
  
url = "https://api.chapa.co/v1/transaction/initialize"
payload = {
    "amount": "10",
    "currency": "ETB",
    "email": "abebech_bekele@gmail.com",
    "first_name": "Bilen",
    "last_name": "Gizachew",
    "phone_number": "0912345678",
    "tx_ref": f"{uuid.uuid4()}",
    "callback_url": "https://webhook.site/077164d6-29cb-40df-ba29-8a00e59a7e60",
    "return_url": "https://www.google.com/",
    "customization": {
        "title": "Payment",
        "description": "I love online payments"
    }
}
headers = {
    'Authorization': 'Bearer CHASECK_TEST-Dfgb6aAXMA5KrIcrwwH1sy4qUJhrAUtM',
    'Content-Type': 'application/json'
}
  
response = requests.post(url, json=payload, headers=headers)
data = response.json()
print(data)
