import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 댓글을 저장할 리스트
comments_data = []

try:
    # 네이버 언론사 편집 페이지로 이동
    driver.get('https://www.naver.com/')
    time.sleep(3)  # 페이지 로딩 대기

    # '언론사편집' 탭 클릭
    media_edit = driver.find_element(By.LINK_TEXT, '언론사편집')
    media_edit.click()
    time.sleep(3)

    # 뉴스 항목 찾기
    news_items = driver.find_elements(By.CSS_SELECTOR, 'div.MediaView-module__media_area___Z4js3')

    for news in news_items:
        # 뉴스 링크 클릭
        news_url = news.find_element(By.CSS_SELECTOR, 'a.MediaContentsView-module__link_thumb___KldTl').get_attribute("href")
        driver.get(news_url)
        time.sleep(2)  # 페이지 로딩 대기

        # 댓글 추출 (모든 베스트 댓글 가져오기)
        while True:
            comments = driver.find_elements(By.CLASS_NAME, 'u_cbox_list')  # 댓글 리스트 가져오기
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

            # 다음 페이지로 이동하기
            try:
                next_button = driver.find_element(By.CLASS_NAME, 'u_cbox_next')  # '다음' 버튼 찾기
                if "disabled" in next_button.get_attribute("class"):
                    break  # 다음 버튼이 비활성화 상태이면 루프 종료
                next_button.click()  # '다음' 버튼 클릭
                time.sleep(2)  # 페이지 로딩 대기
            except Exception:
                break  # '다음' 버튼이 없거나 클릭할 수 없으면 루프 종료

        driver.back()  # 이전 페이지로 돌아가기
        time.sleep(2)  # 페이지 로딩 대기
        driver.get('https://www.naver.com/')  # 메인 페이지로 다시 이동
        time.sleep(2)

finally:
    driver.quit()  # 드라이버 종료

# DataFrame으로 변환하고 CSV 파일로 저장
df = pd.DataFrame(comments_data)
df.to_csv('comments.csv', index=False, encoding='utf-8-sig')
print("댓글을 comments.csv 파일로 저장했습니다.")

# 크롤링한 댓글 데이터 출력
for comment in comments_data:
    print(comment)
