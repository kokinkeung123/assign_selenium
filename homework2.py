from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)

# try:

url = ("https://www.google.com")
driver.get(url)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("python3")
search_box.send_keys(Keys.RETURN)

time.sleep(3)
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))

first_result = driver.find_element(By.CSS_SELECTOR, "h3")
first_result.click()

# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))

time.sleep(3)

# WebDriverWait(driver, 5).until(lambda d:d.execute_script('return document.readyState') == 'complete')

driver.close()


