#!/usr/bin/python

import requests
import sys
import time
import os 
from datetime import datetime

"""
TODO: Live updating clock
TODO: Format output better, evaluate string length of longest coin
TODO: Add functionality to selectively view data elements (i.e. pct_chage, mkt_cap, 24h_volume)

"""

# fetch data function
def get_data():
    
    # coinmarketcap price data api
    if currency.upper() in valid_currencies:
        api = "https://api.coinmarketcap.com/v1/ticker/?convert=" + currency + "&limit=" + str(num_to_show)

    # turn api data into json
    market_data = requests.get(api).json()

    return market_data

# clear screen based on platform
os.system('cls' if os.name == 'nt' else 'clear')

# some formatting
print("Fudder - CrpytoCurrency Prices Live Inside Your Terminal")
print("--------------------------------------------------------")
print(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

while True:

    # list of fiat currencies supported by the CoinMarketCap API
    valid_currencies = ["AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", 
                        "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", 
                        "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", 
                        "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "USD", "ZAR"]

    # accept / set default system arguments
    try:
        # number of currencies to show
        num_to_show = int(sys.argv[1]) 

        # currency to show dollar amount in
        currency = str(sys.argv[2])  

    # set default listing amount to 10 and default currency to USD
    except IndexError:
        num_to_show = 10
        currency = 'USD'

    # store api data as python variable
    json_data = get_data()
    time.sleep(7) 

    # navigation loop
    for coin in json_data:
        for i in range(1, num_to_show):
            max_length = max(coin['name'], key=len)
        name = coin['name']
        rank = coin['rank']
        pct_change = coin['percent_change_1h']
        price = coin['price_' + currency.lower()]
        print(rank + ". " + name + " - " + "$" + str(round(float(price), 2)) + " " + currency + " " + pct_change + "%")

    print("--------------------------------------------------------")