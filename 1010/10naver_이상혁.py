import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Naver 메인 페이지 URL
url = 'https://www.naver.com/'

# WebDriver 초기화
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

try:
    # 검색 입력 필드가 로드될 때까지 대기
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'query'))
    )
    
    # 검색어 입력 및 엔터 키 누르기
    search_box.send_keys('파이썬' + Keys.ENTER)
    
    # 검색 결과 페이지 로드 대기 (Naver의 메인 검색 결과 컨테이너)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'main_pack'))
    )
    
    # 페이지 소스 가져오기
    mydata = driver.page_source
    soup = BeautifulSoup(mydata, 'html.parser')
    
    # 검색 결과 출력 (예: 뉴스 제목 추출)
    news_titles = soup.select('a.news_tit')  # 뉴스 제목의 CSS 선택자
    for idx, title in enumerate(news_titles, start=1):
        print(f"{idx}. {title.get_text()}\n   링크: {title.get('href')}\n")

finally:
    # 브라우저 종료
    driver.quit()
