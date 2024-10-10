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



#Marker함수 Circle
# folium.CircleMarker(
#     location=[37.5559448,126.93478355],
#     radius = 100,
    
#     tooltip="빅데이터 AI",
#     popup="시청근처 덕수궁",
#     icon=folium.Icon(icon="cloud")
# ).add_to(m)

folium.CircleMarker(
    location = [37.5633295, 126.9747869],
    radius = 700,
    fill = True,    
    color = 'red',
    tooltip="빅데이터 AI",
    popup="시청", #클릭시 나오는 안내문
    icon=folium.Icon(icon="cloud")
).add_to(m)






folium.LayerControl().add_to(m)


path = './data/01map.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('01map.html 테스트')
print()
