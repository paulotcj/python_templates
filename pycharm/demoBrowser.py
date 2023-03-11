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

# specify the amount of time the WebDriver instance i.e. the driver should wait when searching for an element if it is not immediately present in the HTML DOM
driver.implicitly_wait(5)
# --------------------


# --------------------




time.sleep(3)
driver.close()