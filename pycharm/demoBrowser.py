from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()

driver.maximize_window()
url = "https://www.selenium.dev/selenium/web/web-form.html"
driver.get(url)
print(driver.current_url)

# --------------------
# driver.implicitly_wait(0.5)
element = driver.find_element(by=By.ID, value="my-text-id")
element.send_keys("test")
# time.sleep(1)
element = Select( driver.find_element(by=By.NAME, value="my-select"))
element.select_by_visible_text("Two")


element = Select( driver.find_element(by=By.NAME, value="my-select"))
element.select_by_visible_text("Two")


element = driver.find_element(by=By.NAME, value="my-datalist")
element.send_keys("s")


# element = Select( driver.find_element(by=By.NAME, value="my-datalist"))
# element.send_keys("s")

# --------------------
url = "https://demoqa.com/automation-practice-form/"
driver.get(url)
print(driver.current_url)
driver.implicitly_wait(3)
element = driver.find_element(by=By.ID, value="subjectsInput")

element.send_keys("c")
element.send_keys(Keys.BACK_SPACE)
time.sleep(3)

# ------------------

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "subjectsInput"))).send_keys('m')

element = driver.find_element(by=By.ID, value="subjectsInput")
element.send_keys("m")

elusive_el = driver.find_element(by=By.CSS_SELECTOR, value=".subjects-auto-complete__menu")

# time.sleep(10)
# elusive_el = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".subjects-auto-complete__menu")))
# print(elusive_el.get_attribute('outerHTML'))

maths_option = elusive_el.find_element(By.XPATH, "//div[text()='Maths']")
maths_option.click()
print('selected maths')



time.sleep(3)
driver.close()