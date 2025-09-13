# Simple example of using the Coingecko API to retrieve 
# the current price of Bitcoin in US Dollar

import requests

# Define the API endpoint
url = "https://api.coingecko.com/api/v3/simple/price"

# Set the parameters
params = {
    "ids": "bitcoin",         # Coin ID
    "vs_currencies": "usd"    # Target currency
}

# Make the request
response = requests.get(url, params=params)

# Parse the JSON response
data = response.json()

# Display the result
print(f"Bitcoin price in USD: ${data['bitcoin']['usd']}")
