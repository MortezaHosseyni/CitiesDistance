from geopy.geocoders import Nominatim
from geopy import distance
from bs4 import BeautifulSoup
import requests
import re
import folium


# Find romania cities name & location
cities = []

url = requests.get("https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Romania")
soup = BeautifulSoup(url.text, 'html.parser')
td = soup.find_all("td", {"style": "background-color:#FFE6BD"})

for item in td:
    city = re.search('<b>.*">(.*)</a></b>', str(item))
    if city:
        cities.append(city.group(1))

    
    
    
# Find cities location
locations = []

geoLocater = Nominatim(user_agent="geoapiExercises")

for loc in cities:
    l = geoLocater.geocode(loc)
    locations.append((l.latitude, l.longitude))

        
for c in locations:
    print(c)
    print("--------------")