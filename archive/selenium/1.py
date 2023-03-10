from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

import time


driver = webdriver.Chrome()


print("--------------------------------")


url = "https://en.wikipedia.org/wiki/MainPage"

driver.get(url)

#---
element_query = "searchInput"
element = driver.find_element(By.ID, element_query)
#---
# element_query = '//*[@id="searchInput"]'
# element = driver.find_element(By.XPATH, element_query)
#---
# element_query = '/html/body/div[1]/div/header/div[2]/div/div/form/div/input[1]'
# element = driver.find_element(By.XPATH, element_query)


element.send_keys("Python")
element.send_keys(Keys.ENTER)

# element.submit()
# element.click()



# element_query = '//*[@id="searchform"]/div/button'
# element_query = '/html/body/div[1]/div/header/div[2]/div/div/div/form/div/button'
# element = driver.find_element(By.XPATH, element_query)
# element.click()

# ActionChains(driver).move_to_element(element).pause(1).send_keys("22222").perform()



print("--------------------------------")
time.sleep(20)
driver.close()
driver.quit()