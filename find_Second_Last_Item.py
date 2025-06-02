import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


def dismiss_google_password_alert():
    try:
        time.sleep(2)  # Wait for the popup to appear
        pyautogui.press('tab')
        # pyautogui.press('tab')
        pyautogui.press('enter')
    except Exception as e:
        print(f"No popup or error found while dismissing: {e}")


dismiss_google_password_alert()
time.sleep(2)
itemLists = driver.find_elements(By.XPATH, "//div[@class='inventory_item']")

secondItem = itemLists[-2]
item_name_element = secondItem.find_element(By.XPATH, ".//div[@class ='inventory_item_name ']")
print("Last Second Item Name is: ", item_name_element.text)
item_name_element.click()

# if len(itemLists) >= 2:
#     secondItem = itemLists[-2]
#     item_name_element = secondItem.find_element(By.XPATH, ".//div[@ class ='inventory_item_name ']")
#     print("Last Second Item Name is: ", item_name_element.text)
#     item_name_element.click()
# else:
#     print("Not enough items found to select the second last one.")

time.sleep(2)
driver.quit()
