import requests


session = requests.Session()
session.headers.update({
            'X-CMC_PRO_API_KEY': '37d7afe0-e4a2-43f8-83d7-638f2fab929a'
        })

r = requests.get('https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest',headers=session.headers)
print(r.text)