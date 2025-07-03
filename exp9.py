from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
import time

service = Service("C:\\WebDriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

service = Service("C:\\WebDriver\\geckodriver-win64\\geckodriver.exe")
driver = webdriver.Firefox(service=service)

service = Service("C:\\WebDriver\\edgedriver-win64\\edgedriver.exe")
driver = webdriver.Edge(service=service)

time.sleep(5)
driver.quit()
