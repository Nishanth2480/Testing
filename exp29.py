import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = uc.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in")
wait = WebDriverWait(driver, 10)

sign_in_link = wait.until(EC.element_to_be_clickable((By.ID,"nav-link-accountList"))).click()
email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
email_input.send_keys("nishanth.premkumar@gmail.com") 
email_enter =  wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

try:
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[1]/input")))
    password_input.send_keys("Dark$2004")
    time.sleep(3)
    sign_in = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[2]/span/span/input"))).click()
except Exception as e:
    print("Could not enter password or click sign-in:", e)
else:
    print("Password entered and sign-in clicked.")

search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
search.send_keys("Asus Tuf A15 Rtx 4050")
search.send_keys(Keys.ENTER)
time.sleep(3)

fresh_sign_in_link = wait.until(EC.presence_of_element_located((By.ID, "nav-link-accountList")))
ActionChains(driver).move_to_element(fresh_sign_in_link).perform()
sign_out = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-item-signout']/span")))
sign_out.click()
time.sleep(3)

driver.execute_script("alert('Signed out successfully!');")
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

driver.get("https://www.amazon.in")

time.sleep(2)
driver.quit()