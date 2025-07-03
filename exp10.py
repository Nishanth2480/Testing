from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time

service = Service("C:\\WebDriver\\geckodriver-win64\\geckodriver.exe")
driver = webdriver.Firefox(service=service)
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.XPATH,'//*[@id="hobbies"]').click()
time.sleep(10)
driver.close()
