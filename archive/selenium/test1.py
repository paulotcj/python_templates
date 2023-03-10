from selenium import webdriver
from selenium.webdriver.common.by import By

local_chrome_path = "xxxxxxxxxxxxxxxx"

# driver = webdriver.Chrome(executable_path=local_chrome_path)

driver = webdriver.Chrome()


print("--------------------------------")


# result = driver.get("https://www.amazon.com")

# print(result)
print("--------------------------------")

url = "https://www.amazon.ca/Halls-Extra-Strong-Menthol-Count/dp/B07HMD5MBQ"

driver.get(url)

price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")

price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")

price = f"{price_whole.text}.{price_fraction.text}"

print(price)

print("--------------------------------")


url = "https://www.empireonline.com/movies/features/best-movies-2/"

driver.get(url)

# elements = driver.find_elements(By.CLASS_NAME, "jsx-4245974604")

# for i in elements:
#     print(i.text)


elements = driver.find_elements(By.CSS_SELECTOR, "div h3")

for i in elements[::-1]:
    print(i.text)

print("--------------------------------")

driver.close()
driver.quit()