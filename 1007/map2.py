import folium
import webbrowser
import os
import time


# 2번째 지도map
# folium.Map((45.5236, -122.6750), tiles="cartodb positron")
m=folium.Map([37.5564234,126.9240735], zoom_start=14,  tiles="cartodb positron")
# 캐나다 m = folium.Map(location=(45.5236, -122.6750)) 
path ='./data/test2.html' 
m.save(path) 
webbrowser.open(os.path.realpath(path))

time.sleep(1)
print('test2.html문서 ok')
print()