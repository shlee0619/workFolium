import folium
import json
import requests
from folium.plugins import MarkerCluster
import pandas as pd
import webbrowser
import os


p = pd.read_csv('./data/police.csv')
c = pd.read_csv('./data/crime_anal_norm.csv')

# Load Seoul's geojson data for administrative boundaries
seoul_geo_url = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'
seoul_geo = json.loads(requests.get(seoul_geo_url).content)

# Create a base map centered on Seoul
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11, tiles="cartodb positron")

# Add choropleth for crime rate by district using data from 'crime_anal_norm.csv'
folium.Choropleth(
    geo_data=seoul_geo,
    name="Choropleth - Crime Rate by District",
    data=c,
    columns=["구별", "범죄"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Normalized Crime Rate"
).add_to(m)

# Add police station markers with clustering
marker_cluster = MarkerCluster().add_to(m)
for idx, row in p.iterrows():
    folium.Marker(
        location=[row["위도"], row["경도"]],
        tooltip=row["경찰서"],
        popup=row["주소"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(marker_cluster)

# Add layer control
folium.LayerControl().add_to(m)

# Save the map to an HTML file and open it for preview
output_path = './data/Seoul_Crime_Police_Map.html'
m.save(output_path)
webbrowser.open(os.path.realpath(output_path))