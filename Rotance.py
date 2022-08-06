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
    locations.append([l.latitude, l.longitude])



    
# Mark cities on map
map = folium.Map(location=[45.9023988, 24.3881119], zoom_start = 8)
counter = 0
for point in locations:
    folium.Marker(location=point, popup = cities[counter], icon=folium.Icon(color = 'blue')).add_to(map)
    counter = counter + 1

map.save("map.html")