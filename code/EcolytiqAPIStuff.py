import requests
from requests.auth import HTTPBasicAuth

#Our credentials
clientID = "8xhnfmUlVHPdhYYLw6m3rD3UIDU4egH69bGw"
clientSecret = "ZTF8O94xdl1wVG7dJgpqxHYUzbhOCuo6TrZ2UB1qPSl1HNRR"
tokenUrl = "https://api.staging.ecolytiq.arm.ecolytiq.network/oauth/token"

#Access token request
response = requests.post( tokenUrl,
    auth=HTTPBasicAuth(clientID, clientSecret),
    data={
        'grant_type': 'client_credentials',
        'scope': 'all'
    }
)

#Checking if request is successful:
if response.status_code == 200:
    access_token = response.json()['access_token']
    print("Token request successful!")
    print("Access Token:", access_token)
else:
    print("Failed to get access token:", response.json())

#Test transaction data. Please change to the data later
transaction_data = {
    "transactions": [
        {
            "transaction_id": "62c12ecc-17d7-469f-9ecc-b08e00eb8c90",
            "account_id": "a083e879-b37c-4307-9407-a9825d82800b",
            "category": {
                "system": "ECOLYTIQ_V2",
                "value": "ex:transport.flight"
            },
            "co2_model": "DE",
            "amount": {
                "value": -2854,
                "currency_code": "EUR"
            },
            "datetime": "2022-05-15T14:18:34Z"
        },
        {
            "transaction_id": "fa2e6d26-fb0f-49f5-bc8d-ccedbc1ca084",
            "account_id": "a083e879-b37c-4307-9407-a9825d82800b",
            "category": {
                "system": "ECOLYTIQ_V2",
                "value": "ex:transport.servicestations"
            },
            "amount": {
                "value": -192.6,
                "currency_code": "EUR"
            },
            "co2_model": "DE",
            "datetime": "2022-09-05T11:18:34Z"
        }
    ]
}

#Sending transaction data
apiUrl = 'https://api.staging.ecolytiq.arm.ecolytiq.network/transactions/v1/transactions'
response = requests.post(
    apiUrl,
    headers={
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    },
    json=transaction_data
)

# Check if the request was successful
if response.status_code == 200:
    transaction_result = response.json()
    print("Transaction Result:", transaction_result)
else:
    print("Failed to send transaction:", response.json())



