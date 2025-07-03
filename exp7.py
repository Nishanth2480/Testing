from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("C:\\WebDriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://demo.automationtesting.in/Alerts.html")

alert_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@onclick='alertbox()']"))
)
alert_button.click()

WebDriverWait(driver, 10).until(EC.alert_is_present())
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(2)

driver.get("https://www.youtube.com")
time.sleep(2)

driver.switch_to.new_window('tab')
driver.get("https://www.wikipedia.org")
time.sleep(2)

driver.switch_to.window(driver.window_handles[0])
time.sleep(2)

driver.get("https://www.w3schools.com/html/html_links.asp")

try:
    top_link = driver.find_element(By.LINK_TEXT, "Top")
    top_link.click()
except:
    pass

time.sleep(2)

driver.quit()