from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

service = Service("C:\\WebDriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

action = ActionChains(driver)

driver.maximize_window()
driver.get("http://primevideo.com/")
time.sleep(2)
search = driver.find_element(By.XPATH , "/html/body/div/div[1]/div[2]/div/header/nav/div[1]/div/div[2]/ul/li[1]/div/button/span")
action.move_to_element(search).click().perform()
time.sleep(5)
search_bar = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/header/nav/div[1]/div/div[2]/ul/li[1]/div[1]/div/div/div/div/form/input[2]")
search_bar.send_keys("Master")
search_bar.send_keys(Keys.RETURN)
time.sleep(3)
Master_title = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[4]/main/div/div/div[4]/div[2]/ul/article[1]/section/div/a").click()
driver.execute_script("window.scrollTo(0, 100);")
time.sleep(5)
screenshot_dir = r"C:\Users\Arcknight\Desktop\HCL_Testing_Training\Coding\Screenshot"
os.makedirs(screenshot_dir, exist_ok=True)            
screenshot_path = os.path.join(screenshot_dir, "amazon_prime_test.png")
driver.save_screenshot(screenshot_path)
time.sleep(5)
driver.close()