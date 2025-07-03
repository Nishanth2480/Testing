from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:\\WebDriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.primevideo.com/")
time.sleep(2)
search=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/header/nav/div[1]/div/div[2]/ul/li[1]/div").click()
search_input = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/header/nav/div[1]/div/div[2]/ul/li[1]/div[1]/div/div/div/div/form/input[2]")
search_input.send_keys("Master")
search_input.send_keys(Keys.ENTER)

time.sleep(10)
driver.close()