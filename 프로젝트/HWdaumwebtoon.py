# 14selenium.py =  selenium 접근


import time
import pandas as pd  
import numpy as np  

from selenium import webdriver
from selenium.webdriver.common.by  import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome  import ChromeDriverManager

options = webdriver.ChromeOptions( )
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
print('naver webtoon testing  start ~~~  ')

url = 'https://comic.naver.com/webtoon/detail?titleId=823285&no=26'
driver.get(url)
time.sleep(2)
driver.execute_script('window.scrollTo(0, (document.body.scrollHeight)-2700);')


comment = driver.find_elements(by=By.CLASS_NAME, value='u_cbox_comment')    #'u_cbox_comment'
print()


result_list = [ ]
result_dict = { }
pathjson = './mydata/navercm.json'
# json저장 패스

result = [ ]
pathcsv = './mydata/navercm.csv'
pathtxt = './mydata/navercm.txt'
cmFile = open(pathtxt, mode='w', encoding='utf-8')




for ct in comment:
    nick = ct.find_element(by=By.CLASS_NAME, value='u_cbox_nick').text 
    contents = ct.find_element(by=By.CLASS_NAME, value='u_cbox_contents').text 
    date = ct.find_element(by=By.CLASS_NAME, value='u_cbox_date').text 
    cnt_recomm = ct.find_element(by=By.CLASS_NAME, value='u_cbox_cnt_recomm').text 
    print('닉네임:', nick, ' ', contents,'\t', date,'\t',cnt_recomm)
    print('- '*70)
    result.append( [nick] + [cnt_recomm] )
    #일반 텍스트파일 저장
    cmFile.write(nick+' '+contents+date+cnt_recomm)

# time.sleep(6)
driver.implicitly_wait(5)
driver.close()
print('result리스트 출력')
print(result)
df = pd.DataFrame(result, columns=('nick', 'cnt_recomm'))
df.to_csv(pathcsv, encoding='cp949', mode='w', index=True)
print(pathcsv, '저장 성공했습니다')

print(pathtxt, '저장 성공했습니다')


cmFile.close()


'''
#사이트 직접 복붙
url = "https://www.selenium.dev/selenium/web/web-form.html"
driver = webdriver.Chrome()
driver.get(url)

title = driver.title
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
'''

print()