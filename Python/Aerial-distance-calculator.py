# This program can calculate the Aerial Distance between two cities.

from geopy.geocoders import Nominatim
from geopy import distance

geodecoder = Nominatim(user_agent="python")

print("""
	WELCOME TO AERIAL DISTANCE CALCULATOR!
""")

location1 = input("\tEnter your current location :  ")
location2 = input("\tEnter your destination :  ")

coordinates1 = geodecoder.geocode(location1)
coordinates2 = geodecoder.geocode(location2)

lat1 = coordinates1.latitude
lon1 = coordinates1.longitude
lat2 = coordinates2.latitude
lon2 = coordinates2.longitude

starting = (lat1, lon1)
destination = (lat2, lon2)

dist = distance.distance(starting, destination)
diststr = str(dist)
accdist = diststr.split(".", 2)[0]
print(f"\n\tYour aerial distance would b around {accdist} km (approx).")
