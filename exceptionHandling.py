import time
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
try:
    driver.get("https://www.google.co.in/")
    driver.maximize_window()
    searchBox = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
    searchBox.send_keys("https://sudeepyadav5.github.io/")
    searchBox.send_keys(Keys.ENTER)

except NoSuchElementException as nsee:
    print(f"Element not Found {nsee}")
except TimeoutException as toe:
    print(f"Page load timeout {toe}")
except WebDriverException as wde:
    print(f"Web Driver not Found {wde}")
except Exception as ec:
    print(f"An unexpected error occurred: {ec}")
finally:
    time.sleep(5)
    driver.quit()