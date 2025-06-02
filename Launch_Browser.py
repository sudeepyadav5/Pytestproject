from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize Chrome driver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.co.in/")
#driver.find_element(By, //textarea[@id="APjFqb"])
textbox = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
textbox.send_keys("Sudeep Yadav")
textbox.send_keys(Keys.RETURN)


driver.maximize_window()

# Wait for 10 seconds
time.sleep(10)

# Close the browser
driver.quit()
