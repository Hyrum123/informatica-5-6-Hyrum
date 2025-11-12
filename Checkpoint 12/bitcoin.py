import requests

while True:
    try:
        coins = float(input("How many bitcoins do you want to trade? "))
        break
    except ValueError:
        print("Enter a number fool")
        pass

API_KEY = "27be317712d2e0375eddb213e8dc4cf2fbbbb05662302b9b819757b6f9cb4e8b"

response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey="+API_KEY)