import requests
import sys


if len(sys.argv) == 2:
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()
else:
    print("Missing command-line argument")
    sys.exit()


try:
    results = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=e9500ce1aa4d442727ae6b51b93b204fad9b142808ec063d4d181a56eac282c7"
        )
    data = results.json()

    price = float(data["data"]["priceUsd"])
    print(f"${bitcoins * price:,.4f}")

except requests.RequestException:
    print("Failed request")