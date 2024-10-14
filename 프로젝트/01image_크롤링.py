from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import requests
import os

# 필요한 모듈 임포트
print('import 영역 11111111111111111111111111')

# ChromeOptions 설정
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# WebDriver 실행
driver = webdriver.Chrome(options=options)
url = 'https://pixabay.com/ko/images/search/cat'
driver.get(url)

# 이미지 저장 폴더 생성
os.makedirs('./images', exist_ok=True)

# 올바른 headers 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.100 Safari/537.36',
}

# 이미지 요소가 로드될 때까지 대기
wait = WebDriverWait(driver, 10)

# 제공하신 XPath로 이미지 요소 찾기
img_area_path = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div[5]/div/a/img'

try:
    # 이미지 요소가 나타날 때까지 대기
    img_element = wait.until(EC.presence_of_element_located((By.XPATH, img_area_path)))
    img_url = img_element.get_attribute('src')
    print('이미지 URL:', img_url)
    
    # 이미지 다운로드 및 저장
    response = requests.get(img_url, headers=headers)
    if response.status_code == 200:
        with open('./images/cat_specific.jpg', 'wb') as f:
            f.write(response.content)
        print('이미지 저장 완료: ./images/cat_specific.jpg')
    else:
        print('이미지 다운로드 실패:', img_url)
except Exception as e:
    print('에러 발생:', e)

# WebDriver 종료
driver.quit()
