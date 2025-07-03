import time
import logging
import unittest
import HtmlTestRunner
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(
    filename="C:\\Users\\Arcknight\\Desktop\\HCL_Testing_Training\\Coding\\log\\Amazon_login.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("Amazon Login Script Started")

class AmazonSearchTest(unittest.TestCase):
    def setUp(self):
        try:
            service = Service("C:\\WebDriver\\chromedriver-win64\\chromedriver.exe")
            self.driver = webdriver.Chrome(service=service)
            logging.info("Webdriver is created and started successfully")
        except WebDriverException as e:
            logging.error(f"Webdriver could not be started:{e}")
    
    def test_search_asus_laptop(self):
        try:
            driver =self.driver
            driver.maximize_window()
            driver.get("https://www.amazon.in/")
            logging.info("Opened Amazon.in")
            search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
            logging.info("Search bar is found")
            search.send_keys("Asus Tuf A15 Rtx 4050 6GB")
            logging.info("'Asus Tuf A15 Rtx 4050 6GB' is typed")
            search.send_keys(Keys.ENTER)
            logging.info("Search bar is searching and submitted")
            time.sleep(5)
            driver.execute_script("window.scrollTo(0, 1000);")
            screenshot_dir = r"C:\Users\Arcknight\Desktop\HCL_Testing_Training\Coding\Screenshot"
            os.makedirs(screenshot_dir, exist_ok=True)            
            screenshot_path = os.path.join(screenshot_dir, "test_amazon.png")
            driver.save_screenshot(screenshot_path)
            logging.info("ScreenShot taken")
            time.sleep(2)
            assert "asus" in driver.current_url.lower(),\
            "Search for Asus Tuf A15 Rtx 4050 6GB did not completed properly"
        except TimeoutException:
            logging.error("Time limit Exceeded")
        except NoSuchElementException:
            logging.error("Search bar element not found")
        except AssertionError as ae:
            logging.error(f"Assertion Error:{ae}")
        except Exception as e:
            logging.error("An error have occured:{e}")
    
    def tearDown(self):
        driver = self.driver
        driver.close()
        logging.info("Browser Closed")
    
if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\Arcknight\Desktop\HCL_Testing_Training\Coding\reports"))
    logging.info("HTML Report completed")