import sys
import os
import requests


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


API_KEY = os.getenv("COINCAP_API_KEY")

try:
    response = requests.get(
        f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
    )
    response.raise_for_status()

    data = response.json()
    price = float(data["data"]["priceUsd"])

except requests.RequestException:
    sys.exit("API request failed")


total = bitcoins * price

print(f"${total:,.4f}")
