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
driver.implicitly_wait(5)
# --------------------
element = driver.find_element(By.LINK_TEXT, "Open new window")
element.click()

# url = "https://www.selenium.dev/selenium/web/window_switching_tests/simple_page.html"
# driver.get(url)
# element = driver.find_element(By.XPATH, '/html/body/div')
# print(element.text)
# # should show: Simple page with simple test.

#since we clicked on the link and it opened a new window, we should have 2 windows in total
# therefore, we have our original window at windows[0] and the new window at windows[1]
windows = driver.window_handles
driver.switch_to.window( windows[1] )
element = driver.find_element(By.XPATH, '/html/body/div')
print(element.text)
# should show: Simple page with simple test.


# --------------------




time.sleep(7)
driver.close()