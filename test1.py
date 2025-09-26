import requests
    
url = "https://api.chapa.co/v1/transaction/verify/order-2-09b9d51d"
payload = ''
headers = {
    'Authorization': 'Bearer CHASECK_TEST-Dfgb6aAXMA5KrIcrwwH1sy4qUJhrAUtM'
}
response = requests.get(url, headers=headers, data=payload)
data = response.text
print(data)
