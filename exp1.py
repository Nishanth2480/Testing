from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:\\WebDriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.youtube.com")
expected_title="YouTube"
actual_title = driver.title
assert expected_title in actual_title,f"Title Mismatch!Got'{actual_title}'"
music_link=driver.find_element(By.LINK_TEXT, "Music")
music_link.click()
time.sleep(60)
driver.quit()
