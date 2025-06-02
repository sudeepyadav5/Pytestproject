import json
import time

with open('cred.json', 'r') as file:
    cr = json.load(file)

urls = cr["url"]
uName = cr["uName"]
pwd = cr["pwd"]

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(urls)
driver.maximize_window()

uNameElement = driver.find_element(By.ID, "user-name")
uNameElement.send_keys(uName)

passwordElement = driver.find_element(By.ID, "password")
passwordElement.send_keys(pwd)
driver.find_element(By.ID, "login-button").click()


time.sleep(5)
driver.quit()