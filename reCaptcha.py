import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/contact-us/")
driver.maximize_window()

iframeEle = driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']")
driver.switch_to.frame(iframeEle)
time.sleep(2)
checkBox = driver.find_element(By.XPATH, "//span[@id='recaptcha-anchor']")
checkBox.click()

time.sleep(5)
driver.quit()


