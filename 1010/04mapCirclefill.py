import folium  #pip install folium
import os
import webbrowser
import requests
import json
import pandas as pd 


m = folium.Map(location=[37.5564234,126.9240735] , zoom_start=11)

req = requests.get('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
data = req.content
seoul_geo = json.loads(data)
folium.GeoJson(seoul_geo, name='구역표시').add_to(m)


#Marker함수 Circle/CircleMarker
folium.Circle(
    location=[37.5633295,126.9747869],
    radius = 7000,
    fill = True ,
    color ='red',
    tooltip="빅데이터 AI", 
    popup="시청"
).add_to(m)



path = './data/0908map.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('0908map.html testing...')
print()



'''
https://python-visualization.github.io/folium/latest/getting_started.html
#folium.Choropleth 
state_geo = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
).json()


state_data = pd.read_csv(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_unemployment_oct_2012.csv"
)

'''