# HWsoangfolium.py
# 소상공인 데이터 + 지도folium

import requests
import folium
from folium.plugins import MarkerCluster
import webbrowser
import os
import pandas as pd
import numpy as np 
import json
import time

# 홍대근처 37.5564234, 126.92407345
# 시청근처 37.5564399, 126.9239937
#--------------------------------------------------------------------------------
df = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_서울_202109.csv')
print(df)
print()
print(df.info()) #아래쪽 참고
print()

star = df[df['상호명'].str.contains('스타벅스|스타 벅스|starbucks', na=False)]
print(star)
print()


latitude = 37.5564234 # 위도
longitude = 126.92407345 # 경도
m = folium.Map([latitude, longitude], zoom_start=11)

latlong = star[['위도','경도']]
mc_cluster = MarkerCluster().add_to(m)

#첫번째방법 1111
for lat, long in zip(latlong['위도'], latlong['경도']):
    folium.Marker([lat,long], icon=folium.Icon(color='red')).add_to(mc_cluster)

#공공데이터 접근 import urllib.request Request(), urlopen()
req = requests.get('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
data = req.content
seoul_geo = json.loads(data)
folium.GeoJson(seoul_geo, name='구역표시').add_to(m)

path ='./data/sosang.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('sosang.htm 지도 소상공 tmxkqjrtm 위치 지도출력 testing...')
print()



# #두번째방법 2222
# print('다른방법으로 소상공 요거프레소 위치 지도출력 testing...')
# time.sleep(2)
# for k in star.index:
#     print()
#     k_lat = star.loc[k, '위도']
#     k_long = star.loc[k, '경도']
#     folium.Marker([k_lat,k_long], icon=folium.Icon(color='red')).add_to(m)

# path ='./data/mysosang.html'
# m.save(path)
# webbrowser.open(os.path.realpath(path))
# print('mysosang.htm 지도 소상공 요거스레소 위치 지도출력 testing...')
# print()


# df['상호명_lower'] = df['상호명'].str.lower()
# ediya = df[df['상호명_lower'].str.contains('이디야|이디아|ediya', na=False)]
# print(ediya)
# print()

# df['상호명_lower'] = df['상호명'].str.lower()
# yoger = df[df['상호명_lower'].str.contains('요거프레소|요거 프레소|yogerpresso', na=False)]
# print(yoger)
# print()

# time.sleep(1)
# #세번째방법 3333
# m = folium.Map([37.5564234,126.92407345],zoom_start=11)

# for k in range(len(df)):
#     location = (float(df.loc[k,'위도']),float(df.loc[k,'경도']))
#     name = str(df.loc[k,'상호명'])
#     if '요거프레소' in name:
#         if name == '요거프레소':
#             if str(df.loc[k,'지점명'])!='nan':
#                 name = name + str(df.loc[k,'지점명'])
#         popup = folium.Popup(name+'\n'+str(df.loc[k,'도로명주소']), min_width=50, max_width=200)
#         folium.Marker(location, popup=popup, tooltip=name, icon=folium.Icon(icon='mug-hot',color='black',prefix='fa')).add_to(m)

# path = 'data/youngsosang.html'
# m.save(path)
# webbrowser.open(os.path.realpath(path))
# print('youngsosang.htm 지도 소상공 요거스레소 위치 지도출력 testing...')
# print()