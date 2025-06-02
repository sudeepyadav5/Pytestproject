import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the driver
driver = webdriver.Chrome()  # or use Safari(), Firefox(), etc.
driver.get("https://www.google.com")

# Enter a query into the search box
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium")

# Wait for the auto-suggestions to appear
suggestions_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[role='listbox']"))
)

# Get all suggestion elements
suggestions = driver.find_elements(By.CSS_SELECTOR, "ul[role='listbox'] li span")

# Loop through and click on a desired suggestion (e.g., "selenium webdriver")
time.sleep(2)
for suggestion in suggestions:
    if "selenium webdriver" in suggestion.text.lower():
        suggestion.click()
        break

# Optional: Wait or do more actions after clicking
WebDriverWait(driver, 5).until(EC.title_contains("selenium webdriver"))

# Close browser
time.sleep(5)
driver.quit()
