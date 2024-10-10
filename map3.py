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

# 3번째 지도map
m=folium.Map([37.5564234,126.9240735], zoom_start=12)
folium.Marker(
    location=[37.5559448,126.9347835],
    tooltip="현대백화점",  #팝업안내문
    popup="Mt.YW Meadows",
    icon=folium.Icon(icon="cloud"),
).add_to(m)

folium.Marker(
    location=[37.5633295,126.9747869],
    tooltip="서울시청",  #팝업안내문
    popup="Stree 2Line 1Line",
    icon=folium.Icon(color="red"),
).add_to(m)


path ='./data/test3.html' 
m.save(path) 
webbrowser.open(os.path.realpath(path))
time.sleep(1)
print('test3.html문서 ok')
print()

time.sleep(2)


#4번째 지도map
m=folium.Map([37.5564234,126.9240735], zoom_start=12)  #홍대위치 기본
folium.Circle(
    location=[37.5559448,126.9347835],
    radius = 2000,
    color = 'yellow',
    fill = False,
    tooltip="현대백화점",  #팝업안내문
    popup="Mt.YW Meadows~~~", #클릭하면 popup표시
).add_to(m)

folium.CircleMarker(
    location=[37.5633295,126.9747869],
    radius = 50,
    color = '#abcdef',
    fill = True, 
    fillcolor = '#abcedf',
    tooltip="서울시청***",  #팝업안내문
    popup="Stree 2Line 1Line",
    icon=folium.Icon(color="red")
).add_to(m)

path ='./data/test4.html' 
m.save(path) 
webbrowser.open(os.path.realpath(path))
time.sleep(1)
print('test4.html문서 ok')
print()

