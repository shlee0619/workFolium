import folium
import webbrowser
import os
import time


'''
입력한 주소: 신촌 현대백화점
위도: 37.5559448
경도: 126.9347835

입력한 주소: 서울 시청
위도: 37.5633295
경도: 126.9747869
'''

# 4번째 지도map
m=folium.Map([37.5564234,126.9240735], zoom_start=12)  #홍대위치 기본 
folium.Circle(
    location=[37.5559448,126.9347835],
    radius=3000,
    color='blue',
    fill=True,
    popup="현대백화점~~~",  #클릭하면 popup표시/ tooltip표시안됨
).add_to(m)

folium.CircleMarker(
    location=[37.5633295,126.9747869],
    radius=50,
    color = 'red' ,
    fill = True,
    fillcolor='red' ,
    tooltip="서울시청***",  #팝업안내문
    popup="seoul city",  #클릭하면 popup표시
    icon=folium.Icon(color="blue"),
).add_to(m)


path ='./data/test4.html' 
m.save(path) 
webbrowser.open(os.path.realpath(path))
print('test4.html문서 ok')
print()
time.sleep(2)


import requests #필수 
m = folium.Map(tiles="cartodbpositron")

geojson_data = requests.get("https://raw.githubusercontent.com/python-visualization/folium-example-data/main/world_countries.json").json()
folium.GeoJson(geojson_data, name="hello world").add_to(m)

folium.LayerControl().add_to(m)
path ='./data/test5.html' 
m.save(path) 
webbrowser.open(os.path.realpath(path))
print('test5.html문서 ok world_countries.json')
print()
