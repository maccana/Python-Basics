# 🪙 Getting Started with the CoinGecko API  
### *Retrieve Cryptocurrency Prices with Ease*

Cryptocurrency prices change constantly—and if you're building a project that needs real-time data, the [CoinGecko API](https://www.coingecko.com/en/api) is a fantastic place to start. It's free, open, and beginner-friendly.

This guide will walk you through how to use the API to get the current price of a cryptocurrency like Bitcoin or Ethereum using Python. No prior API experience needed!

---

## 📘 What Is an API?

Let’s break it down:

- **API** = *Application Programming Interface*
- It’s like a waiter at a restaurant: you (the customer) ask for something, and the waiter (the API) brings it from the kitchen (the server).
- In our case, you’ll ask CoinGecko for the price of a coin, and it’ll deliver the answer.

---

## 🧰 What You’ll Need

To follow along, make sure you have:

- ✅ A computer with internet access  
- ✅ Python installed (version 3.x)  
- ✅ A code editor (e.g., VS Code, Notepad++)  
- ✅ The `requests` library (we’ll install it below)  
- ✅ No API key required—CoinGecko’s API is public!

---

## 🐍 Step-by-Step: Get the Price of a Cryptocurrency

### 1️⃣ Install the Requests Library

Open your terminal or command prompt and run:

```bash
pip install requests

```
### 2️⃣ Create Your Python Script

Create a new file called get_price.py and paste the following code:

```python
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

```

### 3️⃣ Run the Script

In your terminal, navigate to the folder where you saved get_price.py, then run:

```python 
python get_price.py
```

Expected output:

```python
Bitcoin price in USD: $26234
```

### 🧾 Understanding the API Response

The API returns data in JSON format. Here’s what the response looks like:

```json
{
  "bitcoin": {
    "usd": 26234
  }
}
```
This means: Bitcoin is currently worth $26,234 in USD.

### 🔄 Try Other Coins and Currencies

You can change the "ids" and "vs_currencies" parameters to get prices for other coins or currencies.

#### Example: Ethereum in EUR

Update the parameters in your script:

```python
params = {
    "ids": "ethereum",
    "vs_currencies": "eur"
}
```

Expected output: 

```code 
Ethereum price in EUR: €1642
```

### Supported Coin IDs

| Coin Name | Coin ID |
| -------- | -------- |
| Bitcoin  | bitcoin  |
| Ethereum  | ethereum  |

