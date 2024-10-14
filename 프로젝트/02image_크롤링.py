from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import requests
import os

#이번엔 전체 크롤링



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
images_container_xpath = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div'

# 이미지 컨테이너 요소 찾기
images_container = wait.until(EC.presence_of_element_located((By.XPATH, images_container_xpath)))

# 이미지 요소들 찾기 (XPath를 사용하여 모든 img 태그 선택)
img_elements = images_container.find_elements(By.XPATH, './/div/a/img')

# 이미지 URL 리스트 생성
image_urls = []
for img in img_elements:
    src = img.get_attribute('src')
    if src and 'pixabay.com' in src and 'placeholder' not in src:
        image_urls.append(src)

# 중복 제거
image_urls = list(set(image_urls))

# 이미지 다운로드 및 저장
for idx, img_url in enumerate(image_urls):
    try:
        response = requests.get(img_url, headers=headers)
        if response.status_code == 200:
            with open(f'./images/cat{idx}.jpg', 'wb') as f:
                f.write(response.content)
            print(f'이미지 저장 완료: ./images/cat{idx}.jpg')
        else:
            print(f'이미지 다운로드 실패: {img_url}')
    except Exception as e:
        print(f'에러 발생: {e}')

# WebDriver 종료
driver.quit()