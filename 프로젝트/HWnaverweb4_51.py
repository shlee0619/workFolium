import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print('네이버 웹툰 댓글 및 답글 크롤링 시작')

# 드라이버 설정 및 초기화
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://comic.naver.com/webtoon/detail?titleId=777767&no=162&week=fri"
driver.get(url)

# 페이지 로딩을 기다립니다.
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "u_cbox_list")))

# 페이지 스크롤 (필요에 따라 조정)
driver.execute_script('window.scrollTo(0, (document.body.scrollHeight)-2300);')
time.sleep(3)  # 추가 로딩 시간 대기

# 전체 댓글 리스트
comments = driver.find_elements(By.CSS_SELECTOR, 'ul.u_cbox_list > li.u_cbox_comment')
comments_data = []

for idx, comment in enumerate(comments, start=1):
    
    # 클린봇 필터가 있는 댓글 패스
    if comment.find_elements(By.CLASS_NAME, 'u_cbox_cleanbot_contents'):
        print(f"{idx}번째 댓글은 '클린봇'이 부적절한 표현을 감지하여 패스합니다.\n")
        continue

    # 댓글 정보 추출
    u_cbox_nick = comment.find_element(By.CLASS_NAME, 'u_cbox_nick').text
    u_cbox_contents = comment.find_element(By.CLASS_NAME, 'u_cbox_contents').text
    u_cbox_date = comment.find_element(By.CLASS_NAME, 'u_cbox_date').text
    u_cbox_cnt_recomm = comment.find_element(By.CLASS_NAME, 'u_cbox_cnt_recomm').text

    # 댓글 데이터 구조에 답글 포함
    comment_entry = {
        '닉네임': u_cbox_nick,
        '내용': u_cbox_contents,
        '날짜': u_cbox_date,
        '추천 수': u_cbox_cnt_recomm,
        '답글': []  # 답글 리스트 추가
    }

    print(f"{idx}번째 댓글:")
    print(f"닉네임: {u_cbox_nick}")
    print(f"내용: {u_cbox_contents}")
    print(f"날짜: {u_cbox_date}")
    print(f"추천 수: {u_cbox_cnt_recomm}\n")

    # 답글 버튼이 있으면 클릭하여 답글 표시
    try:
        reply_button = comment.find_element(By.CLASS_NAME, 'u_cbox_btn_reply')
        driver.execute_script("arguments[0].click();", reply_button)  # 답글 버튼 클릭
        time.sleep(1)  # 답글 목록 로딩 대기

        # `더보기` 버튼이 있는 경우 반복적으로 클릭하여 모든 답글 로드
        while True:
            try:
                more_button = comment.find_element(By.CLASS_NAME, 'u_cbox_btn_more')
                driver.execute_script("arguments[0].click();", more_button)
                time.sleep(1)
            except:
                break  # 더보기 버튼이 없으면 반복 종료

        # 모든 답글을 수집
        try:
            reply_area = WebDriverWait(comment, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'u_cbox_reply_area'))
            )
            replies = reply_area.find_elements(By.CSS_SELECTOR, 'ul.u_cbox_list > li.u_cbox_comment')
            for reply in replies:
                # 클린봇 필터가 있는 답글 패스
                if reply.find_elements(By.CLASS_NAME, 'u_cbox_cleanbot_contents'):
                    continue

                reply_nick = reply.find_element(By.CLASS_NAME, 'u_cbox_nick').text
                reply_content = reply.find_element(By.CLASS_NAME, 'u_cbox_contents').text
                reply_date = reply.find_element(By.CLASS_NAME, 'u_cbox_date').text

                print(f"  └ 답글 닉네임: {reply_nick}")
                print(f"  └ 답글 내용: {reply_content}")
                print(f"  └ 답글 날짜: {reply_date}\n")

                # 답글 정보 저장
                comment_entry['답글'].append({
                    '답글 닉네임': reply_nick,
                    '답글 내용': reply_content,
                    '답글 날짜': reply_date
                })
        except Exception as e:
            print(f"{idx}번째 댓글의 답글 영역을 찾을 수 없습니다. {e}")

    except Exception as e:
        print(f"{idx}번째 댓글에는 답글 버튼이 없습니다.\n")

    # 전체 댓글 데이터에 저장
    comments_data.append(comment_entry)

# 데이터프레임 생성 (답글을 문자열로 변환하여 저장)
df = pd.DataFrame([
    {
        '닉네임': comment['닉네임'],
        '내용': comment['내용'],
        '날짜': comment['날짜'],
        '추천 수': comment['추천 수'],
        '답글': '\n'.join([f"{r['답글 닉네임']}: {r['답글 내용']} ({r['답글 날짜']})" for r in comment['답글']])
    }
    for comment in comments_data
])

# CSV 파일로 저장
df.to_csv('comments_with_replies.csv', index=False, encoding='utf-8-sig')
print("댓글과 답글을 comments_with_replies.csv 파일로 저장했습니다.")

# 웹 드라이버 종료
driver.quit()
