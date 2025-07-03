import unittest
import time
import openpyxl
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "TestReport"
sheet.append(["Test Name", "Status", "Time", "Remarks"])

class AmazonSearchTest(unittest.TestCase):
    
    def setUp(self):
        service = Service("C:\\WebDriver\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_search_asus_laptop(self):
        test_name = "Amazon Asus Search"
        try:
            driver = self.driver
            driver.get("https://www.amazon.in/")
            time.sleep(2)
            search = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
            search.send_keys("Asus Tuf A15 Rtx 4050")
            search.send_keys(Keys.ENTER)
            time.sleep(2)
            self.assertIn("Asus Tuf A15", driver.page_source)
            sheet.append([test_name, "PASS", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Search result found"])
        except Exception as e:
            sheet.append([test_name, "FAIL", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(e)])
            raise

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        workbook.save(r"C:\Users\Arcknight\Desktop\HCL_Testing_Training\Coding\reports\TestResult.xlsx")

if __name__ == '__main__':
    unittest.main()
