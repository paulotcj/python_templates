from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.smashingmagazine.com/2017/05/long-scrolling/"
driver.get(url)
print(driver.current_url)
# specify the amount of time the WebDriver instance i.e. the driver should wait when searching for an element if it is not immediately present in the HTML DOM
# driver.implicitly_wait(5)

# --------------------
driver.execute_script("window.scrollBy(0,1000);")
driver.get_screenshot_as_file("screenshots/1.png")
# time.sleep(1)
driver.execute_script("window.scrollBy(0,1000);")
driver.get_screenshot_as_file("screenshots/2.png")
# time.sleep(1)
driver.execute_script("window.scrollBy(0,1000);")
driver.get_screenshot_as_file("screenshots/3.png")
# time.sleep(1)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshots/azsxdcfvgbhnjmklpoiuytrewsqa4.png")
# --------------------

# time.sleep(2)
driver.close()
#something