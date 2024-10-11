
#HWrestapiNaverNews 에서의 문자열을 추출하기

# 네이버 검색 API 예제 - 블로그 검색
# developer.naver.com 로그인 네이버아이디/비번

import os
import sys
import urllib.request

#추가
import json
import pandas as pd
import re
######developer.naver.com에서 등록하고 나서 복사해 온다.
client_id = "g여러분껏"
client_secret = "eZ여러분꺼"
#############입력받은 부분마 입력#####
# data = input('검색키워드 입력 >>>')
# encText = urllib.parse.quote(data)
encText = urllib.parse.quote("제주 동백")
####################################
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url) #1 단계
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request) # 2 단계
rescode = response.getcode()
if(rescode==200):
    response_body = response.read() #3 단계
    # print(response_body.decode('utf-8'))
    #추가
    result = response_body.decode('utf-8') # 4단계
    print(result)
    items = json.loads(result)['items'] #5단계 ->json문서로 가져온다. items항목만 가져오기
else:
    print("Error Code:" + rescode)

### 여기위까지 코드는 네이버 개발자 모드에서 제공되는 소스 복사해 옴

#추가코딩
item = json.loads(result)['items']
title = []
description = []

for k in range(10):
    title.append(item[k]['title'])
    description.append(item[k]['description'])

df = pd.DataFrame()
df['title'] = title
df['description'] = description
print(df.head())
print()
print('- '*70)
print('- '*70)

for i in range(10):
    df['title'][i] = re.sub('\\\\n','',df['title'][i])
    # df['title'][i] = re.sub('[^가-힣]','',df['title'][i])
    df['title'][i] = re.sub('&lt;&gt;','',df['title'][i])
    #기존에 추가
    df['title'][i] = re.findall('[가-힣]{2,7}',str(df['title'][i]))


for i in range(10):
    df['description'][i] = re.sub('\\\\n','',df['description'][i])
    # df['title'][i] = re.sub('[^가-힣]','',df['title'][i])
    df['description'][i] = re.sub('&lt;&gt;','',df['description'][i])
    #기존에 추가
    df['description'][i] = re.findall('[가-힣]{2,7}',str(df['description'][i]))
    
print(df)
print()
print('df[title]=>',df['title'],type(df['title'])) #Name: title, dtype: object <class 'pandas.core.series.Series'>
print()
print('df[description]=>',df['description'],type(df['description']))
print()

for i in range(len(df['title'])):            # 세로 크기
     for j in range(len(df['title'][i])):     # 가로 크기 a[i] [값, 값]의 len은 2
         print(df['title'][i][j], end=' ')
         print()
print('10-07-monday 제주 동백 블로그 검색끝')

'''
df[title]=> 0                   [금메달, 감이던, 제주, 동백, 수목원, 맛집]
1    [겨울, 제주도, 당일치기, 제주, 동백, 수목원, 명소, 소품샵, 현지인]
2                [제대로, 즐긴, 제주, 동백, 수목원, 맛집, 미향]
3         [제주, 동백, 포레스트, 입장료, 제주도, 동백꽃, 명소, 추천]
4       [제주도, 동백꽃, 명소, 제주, 동백, 포레스트, 수목원, 갈만한곳]
5                     [제주, 여행, 동백, 명소, 동백, 수목원]
6                          [제주, 한림, 맛집, 동백, 키친]
7                     [제주, 동백, 부엌, 제주, 한정식, 맛집]
8      [겨울, 제주도, 여행, 제주, 동백, 명소, 동백포레스트, 동백수목원]
9                         [제주, 제주동백, 수목원, 교래퐁낭]
Name: title, dtype: object <class 'pandas.core.series.Series'>

df[description]=> 0    [끝에, 제주, 동백, 수목원, 맛집에, 방문했는데요, 특수제작한, 불판, 덕에, ...
1    [안녕하세요, 체토입니다, 겨울여행, 하면, 빼놓을, 없는, 제주동백, 이죠, 지금...
2    [제주, 동백, 수목원, 맛집, 제주미향은, 이렇게, 룸도, 따로, 준비되어, 있었...
3    [카페는, 그야말로, 아름다움, 자체였어요, 이렇게, 눈이, 언제, 내릴지, 모르겠...
4    [그리고, 신천목장은, 올해는, 감피, 건조, 작업을, 안하는지, 썰렁했습니다, 제...
5    [제가, 이번에, 다녀온, 곳은, 동백꽃으로, 유명한, 하나인, 동백, 수목원인데요...
6    [되었답니다, 동백키친, 동백키친, 영업시간, 매주, 수요일, 휴무, 오전, 오후,...
7    [커텐도, 동백이다, 제주, 동백, 부엌이란, 상호에, 맞게, 통일된, 인테리어와,...
8    [제주, 동백, 포레스트, 아기자기한, 숲속, 느낌이, 많이, 들었던, 제주도, 동...
9    [그럼, 동백을, 보러, 가볼까요오, 제주도에서, 동백을, 있는, 곳은, 여러, 군...
Name: description, dtype: object <class 'pandas.core.series.Series'>

금메달
감이던
제주
동백
수목원
맛집
겨울
제주도
당일치기
제주
동백
수목원
명소
소품샵
현지인
제대로
즐긴
제주
동백
수목원
맛집
미향
제주 
동백
포레스트
입장료
제주도
동백꽃
명소
추천
제주도
동백꽃
명소
제주
동백
포레스트
수목원
갈만한곳
제주
여행
동백
명소
동백
수목원
제주
한림
맛집
동백
키친
제주
동백
부엌
제주
한정식
맛집
겨울
제주도
여행
제주
동백
명소
동백포레스트
동백수목원
제주
제주동백
수목원
교래퐁낭 
10-07-monday 제주 동백 블로그 검색끝
'''



# a = [[10, 20], [30, 40], [50, 60]]
# for i in range(len(a)):            # 세로 크기
#     for j in range(len(a[i])):     # 가로 크기 a[i] [값, 값]의 len은 2
#         print(a[i][j], end=' ')
#     print()
