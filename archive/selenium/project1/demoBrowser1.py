from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()

driver.maximize_window()
url = "https://en.wikipedia.org/wiki/MainPage"
driver.get(url)
print(driver.current_url)

# --------------------

url = "https://www.google.com"
driver.get(url)
driver.refresh()
driver.back()
driver.minimize_window()
driver.close()
