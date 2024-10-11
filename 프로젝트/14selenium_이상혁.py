# 14selenium.py selenium 기술 응용

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print('네이버 웹툰 테스트')

# 드라이버 설정 및 초기화
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    url = "https://comic.naver.com/webtoon/detail?titleId=802039&no=200&week=mon"
    driver.get(url)

    # 페이지 로딩을 기다립니다.
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "u_cbox_list")))

    # 페이지 스크롤 (필요에 따라 조정)
    driver.execute_script('window.scrollTo(0, (document.body.scrollHeight)-2300);')

    # 추가 로딩 시간을 위해 잠시 대기
    time.sleep(3)

    # 댓글 목록 요소 찾기
    u_cbox_list = driver.find_element(By.CLASS_NAME, 'u_cbox_list')

    # 모든 댓글 요소 찾기
    comments = u_cbox_list.find_elements(By.CLASS_NAME, 'u_cbox_comment')

    print('type(comments) 확인:', type(comments))
    print(f'총 댓글 수: {len(comments)}')

    # 댓글 데이터를 저장할 리스트
    comment_data = []

    for idx, comment in enumerate(comments, start=1):
        try:
            # 닉네임 추출
            u_cbox_nick = comment.find_element(By.CLASS_NAME, 'u_cbox_nick').text
            # 댓글 내용 추출
            u_cbox_contents = comment.find_element(By.CLASS_NAME, 'u_cbox_contents').text
            # 날짜 추출
            u_cbox_date = comment.find_element(By.CLASS_NAME, 'u_cbox_date').text
            # 추천 수 추출
            u_cbox_cnt_recomm = comment.find_element(By.CLASS_NAME, 'u_cbox_cnt_recomm').text

            print(f"{idx}번째 댓글:")
            print(f"닉네임: {u_cbox_nick}")
            print(f"내용: {u_cbox_contents}")
            print(f"날짜: {u_cbox_date}")
            print(f"추천 수: {u_cbox_cnt_recomm}\n")

            # 데이터 저장
            comment_data.append({
                '닉네임': u_cbox_nick,
                '내용': u_cbox_contents,
                '날짜': u_cbox_date,
                '추천 수': u_cbox_cnt_recomm
            })

        except Exception as e:
            print(f"{idx}번째 댓글 처리 중 오류 발생: {e}")

    # 댓글을 DataFrame으로 변환
    df = pd.DataFrame(comment_data)
    # CSV 파일로 저장
    df.to_csv('comments.csv', index=False, encoding='utf-8-sig')
    print("댓글을 comments.csv 파일로 저장했습니다.")

except Exception as e:
    print(f"오류 발생: {e}")

finally:
    driver.quit()
    print("드라이버를 종료했습니다.")
