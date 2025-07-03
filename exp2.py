import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = uc.Chrome()
driver.get("https://www.google.com")

search = driver.find_element(By.NAME, "q")
search.send_keys("chatgpt")
search.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()