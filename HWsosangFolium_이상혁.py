
import pandas as pd
import folium
import webbrowser
import os
import time


path = '소상공인시장진흥공단_상가(상권)정보_서울_202112.csv'
df = pd.read_csv(path,encoding='UTF=8')

print(df[(df['상호명']=='이디야')|(df['상호명']=='스타 벅스')|(df['상호명']=='STARBUCKSCOFFEE')][['상호명','위도','경도']])


m=folium.Map([37.5564234,126.9240735], zoom_start=12) 
for index, row in df[(df['상호명']=='스타벅스') | (df['상호명']=='스타 벅스') | (df['상호명']=='STARBUCKSCOFFEE')].iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],
        tooltip=row['상호명'], 
        popup="스타벅스 매장",  
        icon=folium.Icon(icon="cloud")  
    ).add_to(m)

# 결과 지도 출력
path = "starbucks_map.html"
m.save(path)
webbrowser.open(os.path.realpath(path))
time.sleep(1)
print('test3.html문서 ok')
print()
