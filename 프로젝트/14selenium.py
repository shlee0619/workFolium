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
print('type(comment) 확인' , type(comment))
print('comment[0] 확인' , comment[0])
print()

result = [ ]
nick = comment[3].find_element(by=By.CLASS_NAME, value='u_cbox_nick').text 
contents = comment[3].find_element(by=By.CLASS_NAME, value='u_cbox_contents').text 
date = comment[3].find_element(by=By.CLASS_NAME, value='u_cbox_date').text 
cnt_recomm = comment[3].find_element(by=By.CLASS_NAME, value='u_cbox_cnt_recomm').text 
print('닉네임:', nick, ' ', contents,'\t', date,'\t',cnt_recomm)

time.sleep(6)
driver.close()
print('naver webtoon testing  end종료 ~~~ ')

# selenium접근 현재는 for반복문이 아니라  댓글갯수가 제일많은 상위한건데이터 추출 
# <span class="u_cbox_nick">음</span>
# <span class="u_cbox_contents" style="" data-lang="ko">장녀 나왔을때~~ 정석. 기자매.</span>
# <span class="u_cbox_date"> 2024-09-11 22:59 </span>
# <em class="u_cbox_cnt_recomm">4087</em>




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