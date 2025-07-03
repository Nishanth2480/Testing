from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("C:\\WebDriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.youtube.com/")
print("Opened YouTube")

wait = WebDriverWait(driver, 10)
search = wait.until(EC.visibility_of_element_located((By.NAME, "search_query")))

search.send_keys("ChatGPT")
search.send_keys(Keys.ENTER)
print("Searched for ChatGPT")
time.sleep(3)

driver.get("https://accounts.google.com/")
print("Opened Google Account")
time.sleep(2)

driver.get("https://aniwatchtv.to/recently-updated")
print("Opened AniwatchTV")
time.sleep(2)

driver.back()
print("Back to:", driver.title)
time.sleep(2)

driver.back()
print("Back to:", driver.title)
time.sleep(2)

driver.forward()
print("Forward to:", driver.title)
time.sleep(2)

driver.refresh()
print("Refreshed:", driver.title)
time.sleep(2)

driver.quit()