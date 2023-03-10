from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()

driver.maximize_window()
url = "https://facebook.com/login/"
driver.get(url)
print(driver.current_url)

# --------------------

element = driver.find_element(by=By.ID, value="email")

element.send_keys("username@fakeemail.com")

element = driver.find_element(by=By.ID, value="pass")
element.send_keys("secretpassword")

# this part works, but i am disabling it in order to avoid any kind  of issue
# element = driver.find_element(by=By.ID, value="loginbutton")
# element.click()demoBrowser.py

# time.sleep(20)
driver.close()