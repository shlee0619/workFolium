import folium
import os
import webbrowser
import requests
import json
import pandas as pd

df = pd.read_csv("./data/소상공인시장진흥공단_상가(상권)정보_서울_202109.csv")
print(df)
print()
print(df.info())
print()

m = folium.Map( 
    location = [37.5564234, 126.9240735], 
    zoom_start =11)

for k in range(len(df)):
    location = (float(df.loc[k, '위도']),float(df.loc[k, '경도']))
    name = str(df.loc[k,'상호명'])
    if '요거프레소' in name:
        if  name == '요거프레소':
            if str(df.loc[k, '지점명']) != 'nan':
                name = name + str(df.loc[k,'지점명'])
        popup = folium.Popup(name + '\n' + str(df.loc[k, '도로명주소']), 
                             min_width = 50, max_width=200)
        folium.Marker(location, 
                      popup=popup, 
                      tolltip=name, 
                      icon=folium.Icon(icon='mug-hot',color='black',prefix='fa')
                      ).add_to(m)



print('1층 요거프레소 커피 지도표시 ')
path = './data/01map.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('01map.html 테스트')
print()