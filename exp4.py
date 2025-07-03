from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
service = Service("C:\\WebDriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")
Username = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
Username.send_keys("standard_user")
time.sleep(2)
Password = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
Password.send_keys("secret_sauce")
time.sleep(2)
login = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input")
assert not login.get_attribute("disabled")
login.click()
time.sleep(3)
driver.close()