import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://dummypoint.com/seleniumtemplate.html")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
ddList = driver.find_element(By.XPATH, "//select[@id='dropdown']")
ddSelect = Select(ddList)
ddSelect.select_by_visible_text("Option1")
time.sleep(2)
ddSelect.select_by_index(3)
time.sleep(2)
ddSelect.select_by_value('OptionFive')





time.sleep(5)
driver.quit()