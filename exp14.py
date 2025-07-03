from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select 
import time

service = Service("C:\\WebDriver\\geckodriver-win64\\geckodriver.exe")
driver = webdriver.Firefox(service=service)
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
dropdown_element = driver.find_element(By. ID, "dropdown")
dropdown_element.click()
time.sleep(3)
select = Select(dropdown_element)
select.select_by_visible_text("Option 2")
time.sleep(1)
dropdown_element.click()
select.select_by_index(1)
time.sleep(1)
dropdown_element.click()
select.select_by_value("2")
time.sleep(1)
time.sleep(5)
driver.close()


