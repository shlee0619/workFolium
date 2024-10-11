import folium
import webbrowser
import os
import time


# pip install folium
# 1번째 지도map
# m=folium.Map(location=[37.5564234,126.9240735], zoom_start=14)
# m=folium.Map(location=(37.5564234,126.9240735), zoom_start=14)
m=folium.Map([37.5564234,126.9240735], zoom_start=12)
m=folium.Map([37.5564234,126.9240735], zoom_start=16)
m=folium.Map([37.5564234,126.9240735], zoom_start=14)
path ='./data/test1.html' 
m.save(path) 
time.sleep(1)
webbrowser.open(os.path.realpath(path))
print('test1.html문서 ok')
print()