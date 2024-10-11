import time
import pandas as pd  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 웹 드라이버 설정
driver = webdriver.Chrome()
url = 'https://comic.naver.com/webtoon/detail?titleId=777767&no=162&week=fri'
driver.get(url)
time.sleep(2)  # 페이지 로드 대기
driver.execute_script('window.scrollTo(0, (document.body.scrollHeight) - 2700);')

# 댓글 및 답글 크롤링 함수
def get_comments():
    results = []
    try:
        # 댓글 요소를 기다림
        comments = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'u_cbox_comment'))
        )
        
        for comment in comments:
            try:
                nick = comment.find_element(by=By.CLASS_NAME, value='u_cbox_nick').text
                contents = comment.find_element(by=By.CLASS_NAME, value='u_cbox_contents').text
                date = comment.find_element(by=By.CLASS_NAME, value='u_cbox_date').text
                cnt_recomm = comment.find_element(by=By.CLASS_NAME, value='u_cbox_cnt_recomm').text
                
                results.append([nick, contents, date, cnt_recomm])
                
                # 답글 처리
                reply_area = comment.find_element(By.CLASS_NAME, 'u_cbox_reply_area')
                replies = reply_area.find_elements(By.CLASS_NAME, 'u_cbox_comment')
                
                for reply in replies:
                    try:
                        reply_nick = reply.find_element(by=By.CLASS_NAME, value='u_cbox_nick').text
                        reply_contents = reply.find_element(by=By.CLASS_NAME, value='u_cbox_contents').text
                        reply_date = reply.find_element(by=By.CLASS_NAME, value='u_cbox_date').text
                        reply_cnt_recomm = reply.find_element(by=By.CLASS_NAME, value='u_cbox_cnt_recomm').text
                        
                        results.append([reply_nick, reply_contents, reply_date, reply_cnt_recomm])  # 답글 추가
                    except Exception as e:
                        print(f"답글 처리 중 오류 발생: {e}")

            except Exception as e:
                print(f"댓글 처리 중 오류 발생: {e}")

    except Exception as e:
        print(f"댓글을 찾는 중 오류 발생: {e}")

    return results

# 결과 저장
data = get_comments()
df = pd.DataFrame(data, columns=('닉네임', '내용', '날짜', '추천수'))
df.to_csv('./mydata/navercm.csv', encoding='cp949', index=False)
print('CSV 저장 성공')

driver.quit()
