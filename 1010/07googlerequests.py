# 07googlerequest.py


import time
time.sleep(1)

import requests       #get(), text속성, content속성   content()에러 text()에러
url = 'http://www.google.com'
response2 =  requests.get(url)
print('response2 상태코드 ', response2.status_code)
print('내용 text속성 ', response2.content )
print()
print('내용 text속성 ', response2.text )
print()
