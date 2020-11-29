import json
import requests
import time


while True:
    r = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot', timeout=10)
    data = r.json()
    price = data["data"]["amount"]
    print("The current spot price of BTC in USD is:","$" + str(price) , " Price provided by coinbase API")
    time.sleep(10)