import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import HtmlTestRunner

class AmazonSearchTest(unittest.TestCase):
    
    def setUp(self):
        service = Service("C:\\WebDriver\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_search_asus_laptop(self):
        driver = self.driver
        driver.get("https://www.amazon.in/")
        time.sleep(2)
        search = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
        search.send_keys("Asus Tuf A15 Rtx 4050")
        search.send_keys(Keys.ENTER)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))