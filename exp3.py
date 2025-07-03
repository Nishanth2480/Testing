from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:\\WebDriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.cleartrip.com/")
element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div")
element.click()
time.sleep(30)
