import folium  
import os
import webbrowser
import requests
import json
import pandas as pd 


# HWpoliceMapChopleth.py
# ./data/crime_anal_norm범죄절도cctv.csv  ./data/police경찰서이름주소위도경도.csv


m = folium.Map(location=[37.5564234,126.9240735] , zoom_start=11)

req = requests.get('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
data = req.content
seoul_geo = json.loads(data)
folium.GeoJson(seoul_geo, name='구역표시').add_to(m)


#folium.Choropleth 
'''
state_geo = requests.get( "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json").json()
state_data = pd.read_csv("https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_unemployment_oct_2012.csv")
folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",    fill_color="YlGn",
    fill_opacity=0.7,     line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(m)
'''


path = './data/0908policemap.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('0908policemap.html testing...')
print()


#공공데이터 디코딩  import requests임포트 다시 확인 
'''
fill_color칼라색 참고
'BuGn': 'Sequential',
'BuPu': 'Sequential',
'GnBu': 'Sequential',
'OrRd': 'Sequential',
'PuBu': 'Sequential',
'PuBuGn': 'Sequential',
'PuRd': 'Sequential',
'RdPu': 'Sequential',
'YlGn': 'Sequential',   #권장컬러
'YlGnBu': 'Sequential',
'YlOrBr': 'Sequential',
'YlOrRd': 'Sequential',
'BrBg': 'Diverging',
'PiYG': 'Diverging',
'PRGn': 'Diverging',
'PuOr': 'Diverging',
'RdBu': 'Diverging',
'RdGy': 'Diverging',
'RdYlBu': 'Diverging',
'RdYlGn': 'Diverging',
'Spectral': 'Diverging',
'Accent': 'Qualitative',
'Dark2': 'Qualitative',
'Paired': 'Qualitative',
'Pastel1': 'Qualitative',
'Pastel2': 'Qualitative',
'Set1': 'Qualitative',
'Set2': 'Qualitative',
'Set3': 'Qualitative'
'''