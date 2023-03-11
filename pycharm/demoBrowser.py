from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.selenium.dev/selenium/web/window_switching_tests/page_with_frame.html"
driver.get(url)
print(driver.current_url)
# specify the amount of time the WebDriver instance i.e. the driver should wait when searching for an element if it is not immediately present in the HTML DOM
# driver.implicitly_wait(5)

# --------------------
# # we would be unable to find the element below, because it's inside an iframe
# element = driver.find_element(By.LINK_TEXT, "I go to a target")
# element.click()

# instead we need to execute a 'switch to'
iframe = driver.find_element(By.NAME, 'myframe')
driver.switch_to.frame(iframe)

element = driver.find_element(By.XPATH, '/html/body/div')
print("It should display 'Simple page with simple test.' ->",element.text)



# --------------------

time.sleep(7)
driver.close()