
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
url = 'https://comic.naver.com/webtoon/detail?titleId=823285&no=26'
driver.get(url)
time.sleep(3)
driver.execute_script('window.scrollTo(0, (document.body.scrollHeight)-2700);')

ct = driver.find_elements(by=By.CLASS_NAME, value='u_cbox_comment')    

result = [ ]
nick = ct[0].find_element(by=By.CLASS_NAME, value='u_cbox_nick').text 
contents = ct[0].find_element(by=By.CLASS_NAME, value='u_cbox_contents').text 
date = ct[0].find_element(by=By.CLASS_NAME, value='u_cbox_date').text 
cnt_recomm = ct[0].find_element(by=By.CLASS_NAME, value='u_cbox_cnt_recomm').text 
print('닉네임:', nick, ' ', contents,'\t', date,'\t',cnt_recomm)
print('> ' * 55)

temp = ct[0].find_element(By.CLASS_NAME, value='u_cbox_btn_reply')
temp.click() #진짜 댓글5 버튼클릭선택해서 댓글 펼쳐짐
time.sleep(2)

ctTest = driver.find_elements(by=By.CLASS_NAME, value='u_cbox_comment') 
ct = ctTest[0]

u_cbox_reply_area = ct.find_element(By.CLASS_NAME, value='u_cbox_reply_area')
u_cbox_list = u_cbox_reply_area.find_element(By.CLASS_NAME, value='u_cbox_list')      
u_cbox_comment = u_cbox_list.find_elements(By.CLASS_NAME, value='u_cbox_comment')

for k in  u_cbox_comment:
    # print('답글닉명 : ', k.find_element(By.CLASS_NAME, value='u_cbox_nick').text) 
    # print(k.find_element(By.CLASS_NAME, value='u_cbox_contents').text)
    print(k.find_element(By.CLASS_NAME, value='u_cbox_nick').text, ':',  k.find_element(By.CLASS_NAME, value='u_cbox_contents').text)





# pathtxt = './mydata/navercm.txt'
# cmFile = open(pathtxt, mode='w', encoding='utf-8')
# cmFile.write(nick+' '+contents+' '+date+' '+cnt_recomm+'\n\n')
time.sleep(5)
driver.close()

print()