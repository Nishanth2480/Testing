import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

service = Service("C:\WebDriver\geckodriver-win64\geckodriver.exe")
driver = webdriver.Firefox(service=service)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/broken_images")

images = driver.find_elements(By.TAG_NAME, "img")
broken_images = []

for img in images:
    src = img.get_attribute("src")
    if src:
            response = requests.get(src)
            if response.status_code != 200:
                broken_images.append(src)
                print(f"Broken image found: {src}")
            else:
                print(f"Working image: {src}")

if broken_images:
    print("Total broken images found:", len(broken_images))
    for broken in broken_images:
        print(broken)
else:
    print("No broken images found.")

time.sleep(3)
driver.quit()