import unittest
import time
from datetime import datetime
from reportlab.pdfgen import canvas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

results = []

class AmazonTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("C:\\WebDriver\\chromedriver-win64\\chromedriver.exe"))

    def test_search(self):
        try:
            self.driver.get("https://www.amazon.in/")
            time.sleep(2)
            box = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
            box.send_keys("Asus Tuf A15 Rtx 4050")
            box.send_keys(Keys.ENTER)
            time.sleep(2)
            self.assertIn("Asus Tuf A15", self.driver.page_source)
            results.append(("Amazon Asus Search", "PASS", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        except Exception as e:
            results.append(("Amazon Asus Search", "FAIL", str(e)))
            raise

    def tearDown(self):
        self.driver.quit()


    def tearDownClass(cls):
        pdf_path = r"C:\Users\Arcknight\Desktop\HCL_Testing_Training\Coding\reports\TestReport.pdf"
        c = canvas.Canvas(pdf_path)
        y = 800
        for name, status, msg in results:
            c.drawString(50, y, f"{name} - {status} - {msg}")
            y -= 20
        c.save()


if __name__ == '__main__':
    unittest.main()
