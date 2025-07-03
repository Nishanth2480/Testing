import os
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

screenshot_dir = r"C:\Users\Arcknight\Desktop\HCL_Testing_Training\Screenshot"
os.makedirs(screenshot_dir, exist_ok=True)

screenshot_path = os.path.join(screenshot_dir, "test_google.png")
driver.save_screenshot(screenshot_path)

driver.quit()
