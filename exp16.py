from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select 
from selenium.webdriver import ActionChains
import time

service = Service("C:\\WebDriver\\geckodriver-win64\\geckodriver.exe")
driver = webdriver.Firefox(service=service)
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
dropdown_element = driver.find_element(By. ID, "dropdown")
dropdown_element.click()
time.sleep(3)
target_value = "Option 2"
select = Select(dropdown_element)
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected Object is {target_value}")
        break
    else:
        print(f"Option'{target_value}'is mismatched")
time.sleep(3)
driver.close()
