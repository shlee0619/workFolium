import urllib.request
import requests
import os
from PIL import Image
from io import BytesIO

print('import from test ok')

# Define the URL and headers
url = 'http://www.google.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# Fetch the webpage
try:
    r = requests.get(url, headers=headers)
    print(r.text)  # Prints webpage content
except requests.RequestException as e:
    print(f"Failed to fetch webpage: {e}")

# Fetch and save the image
image_url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
try:
    r2 = requests.get(image_url)
    image = Image.open(BytesIO(r2.content))
    image.show()

    # Define and create directory if not exists
    image_folder = os.path.join(os.getcwd(), 'images')
    os.makedirs(image_folder, exist_ok=True)

    # Save image
    name = os.path.basename(image_url)
    path = os.path.join(image_folder, name)
    with open(path, 'wb') as file:
        file.write(r2.content)
    print(f"{name} 이미지 저장 성공")

except requests.RequestException as e:
    print(f"Failed to fetch image: {e}")
except IOError as e:
    print(f"Error saving image: {e}")
