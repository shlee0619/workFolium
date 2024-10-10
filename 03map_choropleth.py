import folium #pip install folium
import os
import webbrowser
import requests
import json
import pandas as pd

# m = folium.Map( location = [37.5564234, 126.9240735], zoom_start =12)
m = folium.Map( 
    location = [37.5564234, 126.9240735], 
    zoom_start =12, 
    tiles = 'cartodb positron')

req = requests.get('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
data = req.content
seoul_geo = json.loads(data)
folium.GeoJson(seoul_geo, name='구역표시').add_to(m)


folium.Marker(
    location=[37.5559448,126.93478355],
    tooltip="빅데이터 AI",
    popup="시청근처 덕수궁",
    icon=folium.Icon(icon="cloud")
).add_to(m)

folium.Marker(
    location=[37.5633295, 126.9747869],
    tooltip="데이터베이스",
    popup="홍대입구",
    icon=folium.Icon(color="green")
).add_to(m)

#folium.choropleth
state_geo = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
).json()

state_data = pd.read_csv(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_unemployment_oct_2012.csv"
)

m = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(m)

folium.LayerControl().add_to(m)


path = './data/01map.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('01map.html 테스트')
print()
