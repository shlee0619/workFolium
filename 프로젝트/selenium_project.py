import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 웹드라이버 설정
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 네이버 뉴스 접속
url = 'https://www.naver.com'
driver.get(url)
time.sleep(2)

# '언론사편집' 링크 클릭
editorial_tab = driver.find_element(By.LINK_TEXT, "언론사편집")
editorial_tab.click()
time.sleep(2)

# 뉴스 항목 선택
news_items = driver.find_elements(By.CSS_SELECTOR, 'div.ContentHeaderSubView-module__news_box___dH9b3')

for item in news_items:
    # 언론사 이름
    media_name = item.find_element(By.CLASS_NAME, 'ContentHeaderSubView-module__news_media___YJm6A').text
    # 뉴스 제목
    news_title = item.find_element(By.CLASS_NAME, 'ContentHeaderSubView-module__news_title___wuetX a').text
    # 뉴스 링크
    news_link = item.find_element(By.CLASS_NAME, 'ContentHeaderSubView-module__news_title___wuetX a').get_attribute('href')

    print(f"언론사: {media_name}, 제목: {news_title}, 링크: {news_link}")

