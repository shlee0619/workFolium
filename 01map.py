import folium #pip install folium
import os
import webbrowser
import requests
import json


# m = folium.Map( location = [37.5564234, 126.9240735], zoom_start =12)
m = folium.Map( 
    location = [37.5564234, 126.9240735], 
    zoom_start =12, 
    tiles = 'cartodb positron')




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





path = './data/01map.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('01map.html 테스트')
print()
