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
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.ARROW_DOWN)
checked_count = 0
for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count += 1
expected_checked_count = 9
if checked_count == expected_checked_count:
    print("Checkbox count verified")
else:
    print("Checkbox is mismatched")
time.sleep(10)
driver.close()
