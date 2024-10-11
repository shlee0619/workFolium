
import urllib.request
import json


#1단계
def getRequestURL(url, enc='utf-8'):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    if response.getcode()==200:
        first = response.read()
        print(first)
        print('- ' * 70)

        ret = first.decode(enc)
        print(ret)
    return ret
        

#2단계
def getNatVisitor(returnType, yyyymm, nat_cd, ed_cd ):
    print()
    print('10-07-monday getNatVisitor(returnType,yyyymm, nat_cd, ed_cd ) 함수 ')
    # serviceKey = '400iA9ln1XUUO3jxGMYEKx0ce9vcpw23Ag5htvt0M1Kjiefy%2F1sRLNBogr0aDAjMT9zZ1B9FEsmSbTv19x4r1w%3D%3D'
    serviceKey = '8z5o9xGOhxyngmxrnGripph9YNJNOwLezt%2BZg7N5TGElR0kCxny5TwyxNfqJ6cik8%2Fxa0rl52%2FH823b45CTQAw%3D%3D'    
    url='http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    parameter = '?_type=json&serviceKey='+serviceKey #?_type=json생략하면 에러발생
    parameter =  parameter + '&returnType=' + returnType
    parameter = parameter + '&YM='+yyyymm
    parameter = parameter + '&NAT_CD='+nat_cd
    parameter = parameter + '&ED_CD='+ed_cd
    url = url + parameter
    print(url)
    print()
    ret_data  = getRequestURL(url)
    print()

    print('ㄴ결과 ' , ret_data)
    return json.loads(ret_data)
    

#3단계
result = [ ]
for year in  range(2017, 2018):
    for month in range(1,6):
        yyyymm = '{0}{1:0>2}'.format( str(year), str(month))
        json_data = getNatVisitor('xml', yyyymm, '275', 'E') #275미국국가코드 E=방한외국인 
        if(json_data['response']['header']['resultMsg']=='OK'):
            natKorNm = json_data['response']['body']['items']['item']['natKorNm']
            num = json_data['response']['body']['items']['item']['num']
            print('%s년 %s월 %s %s명' %(str(year), str(month),natKorNm ,num))
            result.append([yyyymm]+[natKorNm]+['275']+[num])          
           

print()
print(result)
print('- ' * 70)
print()


# import urllib.request 라이브러리 
#~~Request(), ~~urlopen(매), ~~read(), ~~decode('utf-8')

import requests

serviceKey = '8z5o9xGOhxyngmxrnGripph9YNJNOwLezt+Zg7N5TGElR0kCxny5TwyxNfqJ6cik8/xa0rl52/H823b45CTQAw=='    
url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
params ={'serviceKey' : serviceKey, 'YM' : '201201', 'NAT_CD' : '112', 'ED_CD' : 'E' }

response = requests.get(url, params=params)
print('response.content 확인 ')
print(response.content)
print()
print('- ' * 70)
print('response.text  확인')
print(response.text)  # text속성 = read() + decode()
print('import requests testing')
