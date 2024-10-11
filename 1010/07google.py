# 07google.py


import urllib.request #Request()생략가능, urlopen(), read(), decode()

url = 'http://www.google.com'
response = urllib.request.urlopen(url)
first = response.read()
print(first)
print()
print('- ' * 70)
print(first.decode('utf-8'))
print('import urllib.request testing END\n')
print(' 🎊 ' * 30)


import time
time.sleep(1)

import requests       #get(), text속성
url = 'http://www.google.com'
response2 =  requests.get(url)
print('response2 상태코드 ', response2.status_code)
print('내용 text속성 ', response2.content )
print()
print('내용 text속성 ', response2.text )
print()
