import urllib.request
import requests
import json
from bs4  import BeautifulSoup
from selenium import webdriver

import pandas as pd
import numpy as np 
import time


# pip install selenium 설치 웹브라우저가동 
# pip install beautifulsoup4 설치  순수하게 사이트주소 tag

# response = urllib.request.urlopen(url)

# url = 'https://www.daum.net/'
# req = urllib.request.urlopen(url)
# first = req.read()
# source = first.decode('utf-8')
# soup = BeautifulSoup(source, 'html.parser')
# print(soup)
# time.sleep(1)

# 새로운 항목 기술
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.naver.com/'
driver = webdriver.Chrome()
driver.get(url) #웹브라우저 열기기능
mydata = driver.page_source
driver.find_element(By.NAME, "query").send_keys("파이썬" + Keys.ENTER)

soup  = BeautifulSoup( mydata , 'html.parser')
print(soup)
time.sleep(5)