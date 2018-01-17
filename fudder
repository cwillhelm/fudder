#!/usr/bin/python

import requests
import sys

"""
TODO: Make persistent (i.e. while true) and update automatically
TODO: Format output better, evaluate length of longest coin
TODO: Add functionality to selectively view data elements (i.e. pct_chage, mkt_cap, 24h_volume)

"""

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

# fetch data function
def get_data():
    
    # coinmarketcap price data api
    if currency.upper() in valid_currencies:
        api = "https://api.coinmarketcap.com/v1/ticker/?convert=" + currency + "&limit=" + str(num_to_show)

    #else:
    #   api = "https://api.coinmarketcap.com/v1/ticker/?convert=?" + "&limit=" + str(num_to_show)

    # turn api data into json
    market_data = requests.get(api).json()

    return market_data

# used for navigating through with for loop
json_data = get_data()

# some formatting
print("Name and Price")
print("--------------")

# navigation loop
for coin in json_data:
    for i in range(1, num_to_show):
        max_length = max(coin['name'], key=len)
    name = coin['name']
    rank = coin['rank']
    pct_change = coin['percent_change_1h']
    price = coin['price_' + currency.lower()]
    print(rank + ". " + name + " - " + "$" + str(round(float(price), 2)) + " " + currency + " " + pct_change + "%")