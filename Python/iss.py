import requests

endpoint = "http://api.open-notify.org/iss-now.json"

resp = requests.get(endpoint).json()

print("Timestamp : ",resp["timestamp"])

print("Longitude : ",resp["iss_position"]["longitude"])

print("Latitude  : ",resp["iss_position"]["latitude"])
