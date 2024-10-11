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
news_items = driver.find_elements(By.CLASS_NAME, value = 'MediaView-module__media_area___Z4js3') #언론사편집 4개의 뉴스상자


# 댓글을 저장할 리스트
comments_data = []

for news in news_items:
    # 뉴스 링크 클릭
    news_url = news.get_attribute("href")  # 뉴스 URL 가져오기
    driver.get(news_url)
    time.sleep(2)

    # 댓글 추출
    comments = driver.find_elements(By.CLASS_NAME, 'u_cbox_list')  # 수정된 부분
    for comment in comments:
        try:
            nick = comment.find_element(By.CLASS_NAME, 'u_cbox_nick').text
            content = comment.find_element(By.CLASS_NAME, 'u_cbox_contents').text
            date = comment.find_element(By.CLASS_NAME, 'u_cbox_date').text
            cnt_recomm = comment.find_element(By.CLASS_NAME, 'u_cbox_cnt_recomm').text
            
            # 댓글 정보를 리스트에 저장
            comments_data.append({
                '닉네임': nick,
                '내용': content,
                '날짜': date,
                '추천수': cnt_recomm
            })
        except Exception as e:
            print(f"댓글 처리 중 오류 발생: {e}")

    driver.back()  # 이전 페이지로 돌아가기
    time.sleep(2)

# DataFrame으로 변환 후 CSV 파일로 저장
df = pd.DataFrame(comments_data)
df.to_csv('comments.csv', index=False, encoding='utf-8-sig')
print("댓글을 comments.csv 파일로 저장했습니다.")

driver.quit()
