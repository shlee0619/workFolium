# 07google

import requests       #get(), text속성
import urllib.request #Reqeust()생략가능, urlopen(), read(), decode()
import json


url='http://www.google.com'
# import urllib.request 접근 decode()
# request = urllib.request.Request(url)
response = urllib.request.urlopen(url)
first = response.read()
print(first)
print()
print('- '*100)
print(first.decode('utf-8'))
print()
print('import urllib.request testing END')
print('- '* 100)


response2 = requests.get(url)
print('response2 상태코드 ', response2.status_code)
print('내용 text속성 ', response2.text)
print()
print()


