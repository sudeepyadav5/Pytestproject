
# import time
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Initialize Chrome WebDriver
# driver = webdriver.Chrome()
# driver.get("https://www.practo.com/plus/corporate")
# driver.maximize_window()
#
# # Give the page some time to load links (optional: you could also wait for a specific element)
# time.sleep(3)
#
# # Find all anchor tags on the page
# all_links = driver.find_elements(By.TAG_NAME, 'a')
#
# # Iterate through each link and check the URL
# for link in all_links:
#     url = link.get_attribute('href')
#     if url and url.startswith("http"):
#         try:
#             response = requests.head(url, timeout=10)
#             if response.status_code < 400:
#                 print(f"✅ Working URL: {url}")
#             else:
#                 print(f"❌ Broken URL: {url} | Status Code: {response.status_code}")
#         except requests.exceptions.RequestException as e:
#             print(f"⚠️ Error accessing {url} | Error: {e}")
#
# # Wait a bit before closing the browser
# time.sleep(5)
# driver.quit()






import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
# Set up Selenium
driver = webdriver.Chrome()
driver.get("https://github.com/jquery")  # or any website you prefer

# Find all <a> tags
all_links = driver.find_elements(By.TAG_NAME, "a")

# Check each link
for link in all_links:
    url = link.get_attribute("href")
    if url:
        try:
            response = requests.head(url, timeout=5)
            if response.status_code < 400:
                print(f"✅ Working: {url}")
            else:
                print(f"❌ Broken: {url} (Status: {response.status_code})")
        except Exception as e:
            print(f"❌ Error with URL: {url} -> {e}")

driver.quit()

# When we have list of url

# import requests
#
# links = [
#     "https://www.wikipedia.org/",
#     "https://the-internet.herokuapp.com/broken_images",
#     "https://demoqa.com/broken",
#     "https://practice.automationbro.com/links/",
#     "sudeep.com"
# ]
#
# for link in links:
#     try:
#         response = requests.head(link, timeout=5)
#         if response.status_code < 400:
#             print(f"✅ Working: {link}")
#         else:
#             print(f"❌ Broken: {link} (Status: {response.status_code})")
#     except Exception as e:
#         print(f"❌ Error with URL: {link} -> {e}")
