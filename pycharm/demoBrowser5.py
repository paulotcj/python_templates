from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.selenium.dev/selenium/web/mouse_interaction.html"
driver.get(url)
print(driver.current_url)

# specify the amount of time the WebDriver instance i.e. the driver should wait when searching for an element if it is not immediately present in the HTML DOM
driver.implicitly_wait(5)
# --------------------
action = ActionChains(driver)
action.move_to_element( driver.find_element(By.ID, "hover") ).perform()
time.sleep(5)
action.drag_and_drop( driver.find_element(By.ID, "draggable"), driver.find_element(By.ID, "droppable") ).perform()


# --------------------




time.sleep(7)
driver.close()