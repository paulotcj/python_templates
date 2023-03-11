from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.maximize_window()
url = "https://www.selenium.dev/documentation/webdriver/interactions/alerts/"
driver.get(url)
print(driver.current_url)

# --------------------
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See an example alert").click()

WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())

alert = driver.switch_to.alert
# print(alert.text)

alert.accept()



# --------------------




time.sleep(3)
driver.close()