import time
import pandas as pd  
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
print('Naver Webtoon testing start ~~~')

url = 'https://comic.naver.com/webtoon/detail?titleId=777767&no=162&week=fri'
driver.get(url)
time.sleep(2)
driver.execute_script('window.scrollTo(0, (document.body.scrollHeight) - 2700);')

# 댓글 및 답글 크롤링
comments = driver.find_elements(by=By.CLASS_NAME, value='u_cbox_comment')
result = []
result_reply = []

pathcsv = './mydata/navercm.csv'
pathtxt = './mydata/navercm.txt'

with open(pathtxt, mode='w', encoding='utf-8') as cmFile:
    for comment in comments:
        try:
            if comment.find_element(by=By.CLASS_NAME, value='u_cbox_delete_contents'):
                 continue
            nick = comment.find_element(by=By.CLASS_NAME, value='u_cbox_nick').text
            contents = comment.find_element(by=By.CLASS_NAME, value='u_cbox_contents').text
            date = comment.find_element(by=By.CLASS_NAME, value='u_cbox_date').text
            cnt_recomm = comment.find_element(by=By.CLASS_NAME, value='u_cbox_cnt_recomm').text
            
            print('닉네임:', nick, ' ', contents, '\t', date, '\t', cnt_recomm)
            print('- ' * 70)
            result.append([nick, cnt_recomm])
            
            # 답글 찾기
            reply_area = comment.find_element(By.CLASS_NAME, 'u_cbox_reply_area')
            replies = reply_area.find_elements(By.CLASS_NAME, 'u_cbox_comment')
                
            for reply in replies:
                try:
                    if reply.find_elements(By.CLASS_NAME, 'u_cbox_delete_contents'):
                        continue 
                    reply_nick = reply.find_element(by=By.CLASS_NAME, value='u_cbox_nick').text
                    reply_contents = reply.find_element(by=By.CLASS_NAME, value='u_cbox_contents').text
                    reply_date = reply.find_element(by=By.CLASS_NAME, value='u_cbox_date').text
                    reply_cnt_recomm = reply.find_element(by=By.CLASS_NAME, value='u_cbox_cnt_recomm').text
                    
                    result_reply.append([reply_nick, reply_contents, reply_date, reply_cnt_recomm])  # 답글 추가
                except Exception as e:
                        print(f"답글 처리 중 오류 발생: {e}")
            # 일반 텍스트파일 저장
            cmFile.write(f"{nick} {contents} {date} {cnt_recomm}\n")
        except Exception as e:
            print(f"댓글 처리 중 오류 발생: {e}")

# CSV 저장
df = pd.DataFrame(result, columns=('nick', 'cnt_recomm'))
df.to_csv(pathcsv, encoding='cp949', mode='w', index=True)
print(f"{pathcsv} 저장 성공했습니다")
print(f"{pathtxt} 저장 성공했습니다")

driver.quit()
