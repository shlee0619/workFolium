import urllib.request 
import requests 
import json
from bs4 import BeautifulSoup
from selenium import webdriver

import pandas as pd
import numpy as np
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# pip install selenium
# pip install beautifulsoup4
# pip install webdriver-manager

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

url = 'https://www.daum.net/'

# 1. urllib을 사용한 웹 페이지 가져오기
try:
    req = urllib.request.urlopen(url)
    first = req.read()
    print(first)
    print()
    
    source = first.decode('utf-8')
    print(source)
    print('- ' * 70)
except Exception as e:
    print(f"URL을 여는 중 오류 발생: {e}")

# 2. BeautifulSoup을 사용한 HTML 파싱
try:
    soup = BeautifulSoup(source, 'html.parser')
    print(soup)
    time.sleep(1)
except Exception as e:
    print(f"BeautifulSoup 파싱 중 오류 발생: {e}")

# 3. Selenium을 사용한 웹 브라우저 자동화 및 요소 상호작용
try:
    # ChromeDriver 자동 설치 및 설정
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)  # 웹 브라우저 열기 기능
    
    # 검색 입력 필드가 로드될 때까지 최대 10초 대기
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'q'))  # 실제 name 속성으로 수정
    )
    
    # 검색어 입력 및 엔터 키 누르기
    search_box.send_keys('파이썬' + Keys.ENTER)
    
    # 검색 결과 페이지 로드 대기 (예: 검색 결과의 특정 요소가 로드될 때까지)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.wrap_cont'))  # 실제 CSS 선택자로 수정
    )
    
    # 페이지 소스 가져오기
    mydata = driver.page_source
    soup = BeautifulSoup(mydata, 'html.parser')
    print(soup)
    
finally:
    # 드라이버 종료
    driver.quit()
