# Write code to select a date from a date picker widget (e.g., book a ticket).

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
iframeEle = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='demo-frame']")))
driver.switch_to.frame(iframeEle)

selectPicker = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='hasDatepicker']")))
selectPicker.click()
myDate = '10/29/1995'
selectPicker.send_keys(myDate)

time.sleep(5)
driver.quit()

