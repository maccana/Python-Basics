#!/usr/bin/env python3

import requests

def fetch_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "ethereum",
        "vs_currencies": "usd"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        print(f"Response: {data}")
        eth_price = data["ethereum"]["usd"]
        print(f"💰 Current Ethereum (ETH) Price: ${eth_price:.2f} USD")
    except requests.RequestException as e:
        print("❌ Error fetching ETH price:", e)

if __name__ == "__main__":
    fetch_eth_price()
