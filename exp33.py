import unittest
import time
import psutil
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AmazonLoginTest(unittest.TestCase):

    def setUp(self):
        chrome_path = r"C:\WebDriver\chromedriver-win64\chromedriver.exe"
        self.driver = webdriver.Chrome(service=Service(chrome_path))
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.in")
        self.wait = WebDriverWait(self.driver, 10)

    def show_alert(self, message):
        self.driver.execute_script(f"alert('{message}');")
        time.sleep(2)
        self.driver.switch_to.alert.accept()

    def login(self, email, password):
        self.wait.until(EC.element_to_be_clickable((By.ID, "nav-link-accountList"))).click()
        email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_input.clear()
        email_input.send_keys(email)
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

        if password != "":
            try:
                password_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
                password_input.clear()
                password_input.send_keys(password)
                self.wait.until(EC.element_to_be_clickable((By.ID, "signInSubmit"))).click()
                time.sleep(2)
            except TimeoutException:
                pass

    def test_valid_credentials(self):
        self.login("nishanth.premkumar@gmail.com", "Dark$2004")
        time.sleep(2)
        if "sign out" in self.driver.page_source.lower() or "your account" in self.driver.page_source.lower():
            self.show_alert("Login successful with valid credentials.")
        else:
            self.show_alert("Login failed even with valid credentials.")
        assert "amazon" in self.driver.title.lower(), "Login failed: Title doesn't contain 'Amazon'"
        assert "sign out" in self.driver.page_source.lower() or "your account" in self.driver.page_source.lower(), \
            "Login failed: Account page not visible"

    def test_invalid_password(self):
        self.login("nishanth.premkumar@gmail.com", "Dark%2004")
        time.sleep(2)
        if "incorrect" in self.driver.page_source.lower() or "problem" in self.driver.page_source.lower():
            self.show_alert("Invalid login credentials detected.")
        else:
            self.show_alert("Login unexpectedly succeeded with wrong password.")
        assert "incorrect" in self.driver.page_source.lower() or "problem" in self.driver.page_source.lower(), \
            "Invalid password not detected."

    def test_empty_password(self):
        self.login("nishanth.premkumar@gmail.com", "")
        time.sleep(2)
        if "enter your password" in self.driver.page_source.lower():
            self.show_alert("Password field is empty.")
        else:
            self.show_alert("No validation message for empty password.")
        assert "enter your password" in self.driver.page_source.lower(), "Empty password validation failed."

    def tearDown(self):
        try:
            account = self.wait.until(EC.presence_of_element_located((By.ID, "nav-link-accountList")))
            ActionChains(self.driver).move_to_element(account).perform()
            sign_out = self.wait.until(EC.element_to_be_clickable((By.ID, "nav-item-signout")))
            sign_out.click()
            time.sleep(1)
        except:
            pass
        self.driver.quit()

        for proc in psutil.process_iter(['pid', 'name']):
            if 'chromedriver' in proc.info['name'].lower():
                proc.kill()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=r"C:\Users\Arcknight\Desktop\HCL_Testing_Training\Coding\reports",
            report_name="amazon_login_report",
            report_title="Amazon Login Test Report"
        )
    )
